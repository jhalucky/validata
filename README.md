# VERIS

veris is a python library designed to validate data widely used in ETL/ELT pipelines to clean-up data records and schemas. It provides set of rules to validate and check data and return the validation report after the validation, it states all the rows and columns which require changes. It doesn't transfrom data, it just validates the data, transformation will come soon. 


## Installation

```bash
pip install veris
```

---

## Quick Start

```python
import pandas as pd

from veris import Validator

df = pd.DataFrame(
    {
        "email": [
            "john@example.com",
            "invalid-email",
            None,
        ],
        "age": [
            25,
            17,
            40,
        ],
    }
)

validator = Validator(df)

validator.column("email") \
    .required() \
    .email()

validator.column("age") \
    .between(18, 60)

result = validator.validate()

print(result.passed)

print(result.errors)
```

---

## Available Rules

### String

- Required
- Email
- Regex
- Min Length
- Max Length
- Length

### Numeric

- Minimum
- Maximum
- Between## Roadmap



## Example Output

```text
ValidationError(
    column="email",
    rule="email",
    failed_rows=[1]
)

ValidationError(
    column="age",
    rule="between",
    failed_rows=[1]
)
```

---


## Documentation

Documentation is currently under active development.

---


## License

Check out the License here [MIT License](LICENSE) 

Copyright (c) 2026 Lucky Jha