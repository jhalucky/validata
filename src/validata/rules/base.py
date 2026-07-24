from __future__ import annotations

from abc import ABC

class BaseRule(ABC):

    name: str = ""

    def __repr__(self) -> str:
        return self.name