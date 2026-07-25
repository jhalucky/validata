from __future__ import annotations

from typing import TYPE_CHECKING



from validata.rules import (
    BaseRule, EmailRule, RequiredRule, UniqueRule, RegexRule, MinLengthRule
)


if TYPE_CHECKING:
    from validata.core.validator import Validator

class ColumnBuilder:

    def __init__(self, validator: Validator, column_name: str) -> None:
        self._validator = validator
        self._column_name = column_name

    def _add_rule(self, rule: BaseRule) -> "ColumnBuilder":

        self._validator._add_rule(
            self._column_name,
            rule
        )

        return self

    def required(self) -> "ColumnBuilder":

        self._add_rule(RequiredRule())

        return self
    
    def email(self):

        self._add_rule(EmailRule())

        return self
    
    
    def unique(self) -> "ColumnBuilder":

        return self._add_rule(
            UniqueRule()
        )
    
    def regex(self, pattern: str) -> "ColumnBuilder":

        return self._add_rule(
            RegexRule(pattern)
        )
    
    def min_length(self, minimum: int) -> "ColumnBuilder":

        return self._add_rule(
            MinLengthRule(minimum)
        )