from veris import Validator

def test_column_returns_builder():
    validator = Validator()

    builder = validator.column("email")

    assert builder is not None


def test_required_rule_is_added():
    validator = Validator()

    validator.column("email").required()

    assert len(validator._rules["email"]) == 1