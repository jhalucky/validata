from __future__ import annotations

class ValidationResult:

    def __init__(self) -> None:
        self.errors : list[dict] = []

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0
    
    def add_error(
            self,
            *,
            column: str,
            rule: str,
            failed_rows: list[int]
    ) -> None:
        
        self.errors.append(
            {
                "column":column,
                "rule":rule,
                "failed_rows":failed_rows
            }
        )