from __future__  import annotations
from abc import abstractmethod

import pandas as pd
from veris.rules.base import BaseRule

class StringRule(BaseRule):

    @abstractmethod
    def is_valid(self, value: str) -> bool:
        """
        Return True if the value satisfies the condition
        """

    def validate(self, column_name: str, series: pd.Series) -> list[int]:

        failed_rows = []


        for index, value in series.dropna().items():

            if not isinstance(value, str):
                failed_rows.append(index)
                continue

            if not self.is_valid(value):
                failed_rows.append(index)


        return failed_rows