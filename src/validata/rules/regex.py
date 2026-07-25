import re
import pandas as pd

from validata.rules.string_rule import StringRule

class RegexRule(StringRule):

    name = "regex"

    def __init__(self, pattern: str):
        self._pattern = re.compile(pattern)


    def is_valid(self, value: str) -> bool:
        return bool(self._pattern.fullmatch(value))