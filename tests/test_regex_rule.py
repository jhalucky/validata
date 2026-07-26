import pandas as pd

from veris import Validator
from veris.result import ValidationError



def test_regex_rule_passes():

    df = pd.DataFrame(
        {
            "employee_id": [
                "EMP-1001",
                "EMP-2045",
                "EMP-9999"
            ]
        }
    )

    validator = Validator(df)

    validator.column("employee_id").regex(
        r"^EMP-\d{4}$"
    )

    result = validator.validate()

    assert result.passed


def test_regex_rule_fails():

    df = pd.DataFrame(
        {
            "employee_id": [
                "EMP-1001",
                "INVALID",
                "EMP-9999"
            ]
        }
    )

    validator = Validator(df)

    validator.column("employee_id").regex(
        r"^EMP-\d{4}$"
    )

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="employee_id",
            rule="regex",
            failed_rows=[1]
        )
    ]



def test_regex_rule_ignores_missing_values():

    df = pd.DataFrame(
        {
            "employee_id": [
                None,
                "EMP-1001",
                None,
                "EMP-2002"
            ]
        }
    )

    validator = Validator(df)

    validator.column("employee_id").regex(
        r"^EMP-\d{4}$"
    )

    result = validator.validate()

    assert result.passed

   
def test_regex_rule_fails_for_non_string_values():

    df = pd.DataFrame(
        {
            "employee_id":[
                1001,
                "EMP-2002"
            ]
        }
    )

    validator = Validator(df)

    validator.column("employee_id").regex(
        r"^EMP-\d{4}$"
    )

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="employee_id",
            rule="regex",
            failed_rows=[0]
        )
    ]