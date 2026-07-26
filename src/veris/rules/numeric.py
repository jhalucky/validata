from __future__ import annotations

import pandas as pd
from abc import abstractmethod

from veris.rules.base import BaseRule

class NumericRule(BaseRule):

    @abstractmethod
    def is_valid(self, value:int | float) -> bool:
        "Return true if numeric value satisfies the rule."

    def validate(self, column_name: str, series: pd.Series) -> list[int]:

        failed_rows = []

        for index, value in series.dropna().items():

            if not (
                isinstance(value, (int, float)) 
                and not isinstance(value, (bool, str))
                ):
                failed_rows.append(index)
                continue

            if not self.is_valid(value):
                failed_rows.append(index)


        return failed_rows
