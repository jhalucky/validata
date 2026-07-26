# Length

The `length()` rule ensures that a string has an exact number of characters.

---

## Syntax

```python
validator.column("code").length(6)
```

---

## Example

```python
validator.column("code") \
    .length(6)
```

---

## Passing Values

| Value |
|-------|
| ABC123 |

---

## Failing Values

| Value |
|-------|
| ABC12 |
| ABC1234 |

---

## Notes

- Useful for IDs, PINs, and fixed-length codes.