from __future__ import annotations

from veris.rules.numeric import NumericRule

class MinimumRule(NumericRule):

    name = "minimum"

    def __init__(self, minimum: int | float):
        self._minimum = minimum

    def is_valid(self, value: int | float) -> bool:
        return value >= self._minimum