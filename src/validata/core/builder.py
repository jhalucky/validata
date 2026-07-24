from __future__ import annotations

from typing import TYPE_CHECKING

from validata.rules.required import RequiredRule
from validata.rules.email import EmailRule
from validata.rules.base import BaseRule


if TYPE_CHECKING:
    from validata.core.validator import Validator

class ColumnBuilder:

    def __init__(self, validator: Validator, column_name: str) -> None:
        self._validator = validator
        self._column_name = column_name

    def required(self) -> "ColumnBuilder":

        self._add_rule(RequiredRule())

        return self
    
    def email(self):

        self._add_rule(EmailRule())

        return self
    
    def _add_rule(self, rule: BaseRule) -> "ColumnBuilder":

        self._validator._add_rule(
            self._column_name,
            rule
        )

        return self