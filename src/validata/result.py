from __future__ import annotations

class ValidationResult:

    def __init__(self) -> None:
        self.errors : list[dict] = []

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0