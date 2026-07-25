import pandas as pd

from validata import Validator
from validata.result import ValidationError

def test_min_length_rule_passes():

    df = pd.DataFrame(
        {
            "username": [
                "alice",
                "bob123",
                "luckyjha"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").min_length(3)

    result = validator.validate()

    assert result.passed


def test_min_length_rule_fails():

    df = pd.DataFrame(
        {
            "username" : [
                "ab",
                "alice",
                "xy"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").min_length(3)

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="username",
            rule="min_length",
            failed_rows=[0,2]
        )
    ]


def test_min_length_rule_ignores_missing_values():

    df = pd.DataFrame(
        {
            "username": [
                "alice",
                "xyz",
                None,
                "lucky",
                None
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").min_length(3)

    result = validator.validate()

    assert result.passed


def test_min_length_rule_fails_for_non_string_values():

    df = pd.DataFrame(
        {
            "username":[
                12223456,
                1234.456,
                "alice"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").min_length(3)

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="username",
            rule="min_length",
            failed_rows=[0, 1]
        )
    ]


def test_min_length_rule_accepts_exacts_boundary():

    df = pd.DataFrame(
        {
            "username": [
                "abc",
                "abcd"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").min_length(3)

    result = validator.validate()

    assert result.passed