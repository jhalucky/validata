# Veris Documentation

Welcome to Veris.

Veris is a lightweight, fluent, and extensible data validation library for Python.

Whether you're validating CSVs, DataFrames, or tabular datasets, Veris provides a clean API to define validation rules and generate clear validation reports.

---

## Documentation

- Getting Started
- Installation
- Quick Start
- Validator
- Rules
- Examples
- Architecture
- Roadmap

---

## Example

```python
from veris import Validator

validator = Validator(df)

validator.column("email") \
    .required() \
    .email()

result = validator.validate()

result.report()