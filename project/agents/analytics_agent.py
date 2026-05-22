"""agents/analytics_agent.py"""
from __future__ import annotations
import re
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Any
from memory.memory_module import MemoryModule


class AnalyticsAgent:
    def __init__(self, memory: MemoryModule):
        self.memory = memory
        self._dataframes: dict[str, pd.DataFrame] = {}

    def register_dataframe(self, name: str, df: pd.DataFrame):
        self._dataframes[name] = df

    def run(self, query: str, memory_context: str = "") -> dict[str, Any]:
        from tools.llm_client import chat_completion
        if not self._dataframes:
            return {"content": "No tabular data loaded. Please upload a CSV or Excel file.", "chart": None}

        schemas = "\n".join(
            f"- {n}: columns={list(df.columns)}, rows={len(df)}"
            for n, df in self._dataframes.items()
        )
        df_sample = next(iter(self._dataframes.values())).head(3).to_string(index=False)

        system = (
            "You are a data analyst. Write Python/Pandas code to answer the user's question.\n"
            f"Available DataFrames:\n{schemas}\n\n"
            f"Sample data:\n{df_sample}\n\n"
            f"Memory:\n{memory_context or 'None'}\n\n"
            "Rules:\n"
            "- Use variable `df` for the main DataFrame\n"
            "- Store the answer string in `result`\n"
            "- If a chart helps, create a Plotly figure in `fig` using plotly.express as px\n"
            "- Do NOT use print()\n"
            "- Return ONLY Python code inside ```python ... ``` block"
        )
        raw = chat_completion(
            [{"role": "system", "content": system}, {"role": "user", "content": query}],
            max_tokens=700,
        )
        code = self._extract_code(raw)
        if not code:
            return {"content": raw, "chart": None}
        return self._execute(code)

    def _extract_code(self, text: str) -> str:
        m = re.search(r"```python\s*(.*?)```", text, re.DOTALL)
        if m:
            return m.group(1).strip()
        if "df" in text or "result" in text:
            return text.strip()
        return ""

    def _execute(self, code: str) -> dict[str, Any]:
        if not self._dataframes:
            return {"content": "No data available.", "chart": None}

        df = max(self._dataframes.values(), key=len)
        local_vars = {"df": df, "pd": pd, "px": px, "go": go, "result": None, "fig": None}

        forbidden = ["import os", "import sys", "open(", "__import__", "subprocess"]
        for f in forbidden:
            if f in code:
                return {"content": f"⚠️ Blocked: forbidden operation '{f}'.", "chart": None}
        try:
            exec(code, local_vars)
        except Exception as e:
            return {"content": f"Analysis error: {e}", "chart": None}

        result = local_vars.get("result")
        fig    = local_vars.get("fig")
        text   = str(result) if result is not None else ("Chart generated." if fig else "Done.")
        return {"content": text, "chart": fig}