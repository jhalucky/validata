from __future__ import annotations

import pandas as pd

from validata.rules.base import BaseRule

class LengthRule(BaseRule):

    name = "length"

    def __init__(self, length: int):
        self._length = length

    def validate(self, column_name: str, series: pd.Series):
        
        failed_rows = []

        for index, value in series.dropna().items():

            if not isinstance(value, str):
                failed_rows.append(index)
                continue

            if len(value) != self._length:
                failed_rows.append(index)


        return failed_rows