import pandas as pd

from veris import Validator
from veris.result import ValidationError

def test_required_rule_passed():

    df = pd.DataFrame(
        {
            "name": ["Lucky","John"]
        }
    )

    validator = Validator(df)

    validator.column("name").required()

    result = validator.validate()

    assert result.passed


def test_required_rule_fails():

    df = pd.DataFrame(
        {
            "name": ["Lucky", None]
        }
    )

    validator = Validator(df)

    validator.column("name").required()

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
        column="name",
        rule="required",
        failed_rows=[1],
    )
]
