import pandas as pd

from veris import Validator
from veris.result import ValidationError

def test_length_rule_passes():

    df = pd.DataFrame(
        {
            "username": [
                "abcdefgh",
                "12345678"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").length(8)

    result = validator.validate()

    assert result.passed

def test_length_rule_fails():

    df = pd.DataFrame(
        {
            "username": [
                "abc",
                "abcdefghij"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").length(8)

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="username",
            rule="length",
            failed_rows=[0,1]
        )
    ]

def test_length_rule_ignores_missing_values():

    df = pd.DataFrame(
        {
            "username": [
                None,
                "abcdefgh",
                None
            ]
        }
    )

    validator = Validator(df)
    validator.column("username").length(8)
    result = validator.validate()

    assert result.passed


def test_length_rule_fails_for_non_string_values():

    df = pd.DataFrame(
        {
            "username": [
                123,
                "abcdefgh",
                12.5
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").length(8)
    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="username",
            rule="length",
            failed_rows=[0,2]
        )
    ]