from __future__ import annotations

from validata.rules.numeric_rule import NumericRule

class BetweenRule(NumericRule):

    name = "between"

    def __init__(self, minimum: int | float, maximum: int|float):
        if minimum > maximum:
            raise ValueError(
                "minimum cannot be greater than maximum"
            )
        
        self._minimum = minimum
        self._maximum = maximum

    def is_valid(self, value: int | float) -> bool:
        return self._minimum <= value <= self._maximum