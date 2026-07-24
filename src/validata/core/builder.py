from __future__ import annotations

from typing import TYPE_CHECKING

from validata.rules.required import RequiredRule
from validata.rules.email import EmailRule


if TYPE_CHECKING:
    from validata.core.validator import Validator

class ColumnBuilder:

    def __init__(self, validator: Validator, column_name: str) -> None:
        self._validator = validator
        self._column_name = column_name

    def required(self) -> "ColumnBuilder":

        self._validator._add_rule(self._column_name, RequiredRule())

        return self
    
    def email(self):

        self._validator._add_rule(
            self._column_name,
            EmailRule()
        )

        return self