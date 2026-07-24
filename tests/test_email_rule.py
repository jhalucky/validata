import pandas as pd

from validata import Validator
from validata.result import ValidationError

def test_email_rule_passes():

    df = pd.DataFrame(
        {
            "email": [
                "lucky@example.com",
                "john@example.org"
            ]
        }
    )

    validator = Validator(df)

    validator.column("email").email()

    result = validator.validate()

    assert result.passed


def test_email_rule_fails():

    df = pd.DataFrame(
        {
        "email": [
            "lucky@example.com",
            "not-an-email"
        ]
        }
    )

    validator = Validator(df)

    validator.column("email").email()

    result = validator.validate()

    assert not result.passed

    assert result.errors == [
        ValidationError(
            column="email",
            rule="email",
            failed_rows=[1]
        )
    ]


def test_email_rule_ignore_missing_values():

    df = pd.DataFrame(
        {
            "email": [
                "lucky@example.com",
                None
            ]
        }
    )

    validator = Validator(df)

    validator.column("email").email()

    result = validator.validate()

    assert result.passed

    