from __future__ import annotations

from veris.core.builder import ColumnBuilder
from veris.result import ValidationResult

class Validator:

    def __init__(self, dataframe=None) ->  None:
        self._dataframe = dataframe
        self._rules: dict[str, list] = {}


    def column(self, column_name: str) -> ColumnBuilder:
        self._rules.setdefault(column_name, [])

        return ColumnBuilder(self, column_name)
    
    def _add_rule(self, column_name: str, rule) -> None:
        self._rules[column_name].append(rule)


    def validate(self) -> ValidationResult:

        result = ValidationResult()

        for column_name, rules in self._rules.items():

            series = self._dataframe[column_name]

            for rule in rules:

                failed_rows = rule.validate(
                    column_name,
                    series
                )

                if failed_rows:

                    result.add_error(
                        column=column_name,
                        rule=rule.name,
                        failed_rows=failed_rows,
                    )
        
        return result