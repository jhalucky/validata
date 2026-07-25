import re
import pandas as pd

from validata.rules.base import BaseRule

class RegexRule(BaseRule):

    name = "regex"

    def __init__(self, pattern: str):
        self._pattern = re.compile(pattern)


    def validate(self, column_name: str, series: pd.Series) -> list[int]:

        failed_rows = []

        for index, value in series.dropna().items():

            if not isinstance(value, str):
                failed_rows.append(index)
                continue

            if not self._pattern.fullmatch(value):
                failed_rows.append(index)

        return failed_rows