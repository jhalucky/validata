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


    def report(self) -> None:

        print("*" * 50)
        print("VALIDATION REPORT")
        print("*"*50)

        status = "PASSED" if self.passed else "FAILED"

        print(f"Status      : {status}")
        print(f"Total Errors: {len(self.errors)}")

        if self.passed:
            return
        
        print()

        for error in self.errors:

            print("*"*50)
            print(f"Column      : {error.column}")
            print(f"Rule        : {error.rule}")
            print(f"Failed Rows : {error.failed_rows}")

        print("-"*50)
