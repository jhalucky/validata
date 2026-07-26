from __future__ import annotations

import pandas as pd
from veris.rules.numeric import NumericRule

class MaximumRule(NumericRule):

    name = "maximum"

    def __init__(self, maximum: int | float):
        self._maximum = maximum

    def is_valid(self, value: int | float) -> bool:
        return value <= self._maximum
