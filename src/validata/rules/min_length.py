from __future__ import annotations

import pandas as pd

from validata.rules.base import BaseRule

class MinLengthRule(BaseRule):

    name = "min_length"

    def __init__(self, minimum: int):

        self._minimum = minimum

    def validate(self, column_name: str, series: pd.Series) -> list[int]:

        failed_rows = []

        for index, value in series.dropna().items():

            if not isinstance(value, str):
                failed_rows.append(index)
                continue

            if len(value) < self._minimum:
                failed_rows.append(index)


        return failed_rows