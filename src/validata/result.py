from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class ValidationError:
    column: str
    rule: str
    failed_rows: list[int]



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
            ValidationError(
                column=column,
                rule=rule,
                failed_rows=failed_rows,
            )
        )

