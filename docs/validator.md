# 4. validator.md

This explains the API.

```md
# Validator

The Validator is the entry point for all validations.

## Creating a validator

```python
validator = Validator(df)
```

## Selecting a column

```python
validator.column("email")
```

## Chaining rules

```python
validator.column("email") \
    .required() \
    .email()
```

## Running validation

```python
result = validator.validate()
```

## Report

```python
result.report()
```

```

---

# Then comes the fun part

Each rule gets its own page.

Example:

```
rules/
    required.md
```

```md
# Required Rule

Checks whether a value is present.

## Example

```python
validator.column("name").required()
```

## Pass

| Value |
|------|
| John |
| Alice |

## Fail

| Value |
|------|
| None |
| "" |

```

