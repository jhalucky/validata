import pandas as pd

from validata import Validator
from validata.result import ValidationError

def test_minimum_rule_passes():

    df = pd.DataFrame(
        {
            "age": [
                18,
                20,
                34
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").minimum(18)
    result = validator.validate()

    assert result.passed 


def test_minimum_rule_fails():

    df = pd.DataFrame(
        {
            "age": [
                15,
                18,
                10
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").minimum(18)
    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="age",
            rule="minimum",
            failed_rows=[0,2]
        )
    ]


def test_minimum_rule_ignores_missing_values():

    df = pd.DataFrame(
        {
            "age":[
                None,
                20,
                None
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").minimum(18)
    result = validator.validate()

    assert result.passed


def test_minimum_rule_fails_for_non_numeric_values():

    df  = pd.DataFrame(
        {
            "age":[
                18,
                "hello",
                True,
                []
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").minimum(18)
    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="age",
            rule="minimum",
            failed_rows=[1,2,3]
        )
    ]


def test_minimum_rule_accepts_boundary():

    df = pd.DataFrame(
        {
            "age": [
                18,
                19
            ]
        }
    )

    validator = Validator(df)
    validator.column("age").minimum(18)
    result = validator.validate()

    assert result.passed