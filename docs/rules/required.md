# Required

The `required()` rule ensures that a value is present.

A value fails validation if it is missing, null, or an empty string.

---

## Syntax

```python
validator.column("name").required()
```

---

## Example

```python
validator.column("name") \
    .required()
```

---

## Passing Values

| Value |
|-------|
| John |
| Alice |
| Bob |

---

## Failing Values

| Value |
|-------|
| None |
| "" |

---

## Notes

- Use this rule for mandatory fields.
- Combine with other rules for more specific validation.