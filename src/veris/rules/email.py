from __future__ import annotations

import re
import pandas as pd

from veris.rules.base import BaseRule

class EmailRule(BaseRule):

    name = "email"

    EMAIL_PATTERN = re.compile(
        r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    )

    def validate(self, column_name: str, series: pd.Series) -> list[int]:
        
        failed_rows: list[int] = []

        for index, value in series.dropna().items():

            if not isinstance(value, str):
                failed_rows.append(index)
                continue

            if not self.EMAIL_PATTERN.fullmatch(value):
                failed_rows.append(index)

        return failed_rows