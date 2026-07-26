from __future__ import annotations

import pandas as pd
from veris.rules.string_rule import StringRule

class LengthRule(StringRule):

    name = "length"

    def __init__(self, length: int):
        self._length = length

    def is_valid(self, value: str) -> bool:
        return len(value) == self._length