from __future__ import annotations

import pandas as pd

from validata.rules import BaseRule

class MaxLengthRule(BaseRule):

    name = "max_length"

    def __init__(self, maximum: int):
        self._maximum = maximum


    def validate(self, column_name: str, series: pd.Series) -> list[int]:

        failed_rows = []

        for index, value in series.dropna().items():

            if not isinstance(value, str):
                failed_rows.append(index)
                continue

            if len(value) > self._maximum:
                failed_rows.append(index)

        return failed_rows