from __future__ import annotations

import pandas as pd
from validata.rules.string_rule import StringRule

class MinLengthRule(StringRule):

    name = "min_length"

    def __init__(self, minimum: int):

        self._minimum = minimum

    def is_valid(self, value: str) -> bool:

        return len(value) >= self._minimum

        