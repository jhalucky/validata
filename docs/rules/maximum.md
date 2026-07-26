# Maximum

The `maximum()` rule ensures that a numeric value is less than or equal to a specified maximum.

---

## Syntax

```python
validator.column("score").maximum(100)
```

---

## Example

```python
validator.column("score") \
    .maximum(100)
```

---

## Passing Values

| Value |
|-------|
| 75 |
| 100 |

---

## Failing Values

| Value |
|-------|
| 101 |
| 150 |

---

## Notes

- Useful when values have an upper limit.