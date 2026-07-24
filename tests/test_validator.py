from validata import Validator

def test_column_returns_builder():
    validator = Validator()

    builder = validator.column("email")

    assert builder is not None