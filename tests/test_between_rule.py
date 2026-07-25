import pandas as pd
import pytest 

from validata import Validator
from validata.result import ValidationError
from validata.rules import BetweenRule

def test_between_rule_passes():

    df = pd.DataFrame(
        {
            "age": [
                18,
                25,
                60
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").between(18,60)
    result = validator.validate()

    assert result.passed


def test_between_rule_fails():

    df = pd.DataFrame(
        {
            "age": [
                15,
                18,
                61,
                70
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").between(18,60)
    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="age",
            rule="between",
            failed_rows=[0,2,3]
        )
    ]


def test_between_rule_fails_for_non_numeric_values():

    df = pd.DataFrame(
        {
            "age": [
                18,
                "hello",
                True,
                []
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").between(18,60)
    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="age",
            rule="between",
            failed_rows=[1,2,3]
        )
    ]


def test_between_rule_ignores_missing_values():

    df = pd.DataFrame(
        {
            "age": [
                None,
                18,
                35,
                None,
            ]
        }
    )

    validator = Validator(df)

    validator.column("age").between(18, 60)

    result = validator.validate()

    assert result.passed



def test_between_rule_accepts_boundaries():

    df = pd.DataFrame(
        {
            "age": [
                18,
                60,
            ]
        }
    )

    validator = Validator(df)

    validator.column("age").between(18, 60)

    result = validator.validate()

    assert result.passed


def test_between_rule_rejects_invalid_range():

    with pytest.raises(ValueError):

        BetweenRule(
            minimum=60,
            maximum=18
        )