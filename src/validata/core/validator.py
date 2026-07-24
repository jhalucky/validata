from __future__ import annotations

from validata.core.builder import ColumnBuilder

class Validator:

    def __init__(self, dataframe=None) ->  None:
        self._dataframe = dataframe
        self._rules: dict[str, list] = {}


    def column(self, column_name: str) -> ColumnBuilder:
        self._rules.setdefault(column_name, [])

        return ColumnBuilder(self, column_name)
