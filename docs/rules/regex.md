# Regex

The `regex()` rule validates values using a regular expression.

---

## Syntax

```python
validator.column("phone").regex(pattern)
```

---

## Example

```python
validator.column("phone") \
    .regex(r"^[0-9]{10}$")
```

---

## Passing Values

| Value |
|-------|
| 9876543210 |

---

## Failing Values

| Value |
|-------|
| abc123 |
| 98-7654 |

---

## Notes

- Use regular expressions for custom formats.