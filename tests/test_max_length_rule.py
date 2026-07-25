import pandas as pd

from validata import Validator
from validata.result import ValidationError

def test_max_length_passes():

    df = pd.DataFrame(
        {
            "username": [
                "theluckyjha",
                "not_amanxx",
                "tomholland2013",
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").max_length(14)

    result = validator.validate()

    assert result.passed


def test_max_length_fails():

    df  = pd.DataFrame(
        {
            "username": [
                "theluckyjhaaaaa",
                "xxxxxxxxx"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").max_length(14)

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="username",
            rule="max_length",
            failed_rows=[0]
        )
    ]


def test_max_length_rule_ignores_missing_values():

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

    validator.column("username").max_length(14)

    result = validator.validate()

    assert result.passed


def test_max_length_rule_fails_for_non_string_values():

    df = pd.DataFrame(
        {
            "username":[
                12223456,
                1234.456,
                "alice",
                "beingsalmankhan"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").max_length(14)

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="username",
            rule="max_length",
            failed_rows=[0,1,3]
        )
    ]


def test_max_length_rule_accepts_exacts_boundary():

    df = pd.DataFrame(
        {
            "username": [
                "abcabcabcabcab",
                "123456789012"
            ]
        }
    )

    validator = Validator(df)

    validator.column("username").max_length(14)

    result = validator.validate()

    assert result.passed
