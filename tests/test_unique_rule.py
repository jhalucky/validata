import pandas as pd

from veris import Validator
from veris.result import ValidationError

def test_unique_rule_passes():

    df = pd.DataFrame(
        {
            "email" : [
                "a@example.com",
                "b@example.com",
                "c@example.com"
            ]
        }
    )

    validator = Validator(df)

    validator.column("email").unique()

    result = validator.validate()

    assert result.passed


def test_unique_rule_fails():

    df = pd.DataFrame(
        {
            "email": [
                "a@example.com",
                "b@example.com",
                "a@example.com"
            ]
        }
    )

    validator = Validator(df)

    validator.column("email").unique()

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="email",
            rule="unique",
            failed_rows=[2]
        )
    ]



def test_unique_rule_ignore_missing_values():

    df = pd.DataFrame(
        {
            "email" : [
                None,
                "a@example.com",
                None,
                "b@example.com"
            ]
        }
    )

    validator = Validator(df)

    validator.column("email").unique()

    result = validator.validate()

    assert result.passed

