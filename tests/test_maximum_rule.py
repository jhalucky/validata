import pandas as pd

from veris import Validator
from veris.result import ValidationError

def test_maximum_rule_passes():

    df = pd.DataFrame(
        {
            "age": [
                18,
                20,
                60
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").maximum(60)
    result = validator.validate()

    assert result.passed



def test_maximum_rule_fails():

    df = pd.DataFrame(
        {
            "age": [
                18,
                65,
                70
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").maximum(60)
    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="age",
            rule="maximum",
            failed_rows=[1,2]
        )
    ]

def test_maximum_rule_ignores_missing_values():

    df = pd.DataFrame(
        {
            "age": [
                18,
                20,
                None
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").maximum(60)
    result = validator.validate()

    assert result.passed


def test_maximum_rule_fails_for_non_numeric_values():

    df = pd.DataFrame(
        {
            "age": [
                18,
                "hello",
                "20",
                []
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").maximum(60)
    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="age",
            rule="maximum",
            failed_rows=[1,2,3]
        )
    ]


def test_maximum_rule_accepts_boundary():

    df = pd.DataFrame(
        {
            "age": [
                60,
                59
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").maximum(60)
    result = validator.validate()

    assert result.passed