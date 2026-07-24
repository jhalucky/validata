from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from validata.core.validator import Validator

class ColumnBuilder:

    def __init__(self, validator: "Validator", column_name: str) -> None:
        self.__validator = validator
        self.__column_name = column_name

