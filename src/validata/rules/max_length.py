from __future__ import annotations

import pandas as pd
from validata.rules.string_rule import StringRule

class MaxLengthRule(StringRule):

    name = "max_length"

    def __init__(self, maximum: int):
        self._maximum = maximum


    def is_valid(self, value: str) -> bool:
        return len(value) <= self._maximum