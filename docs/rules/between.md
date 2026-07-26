# Between

The `between()` rule ensures that a numeric value falls within a specified range (inclusive).

---

## Syntax

```python
validator.column("age").between(18, 60)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| `min` | Minimum allowed value |
| `max` | Maximum allowed value |

---

## Example

```python
validator.column("age") \
    .between(18, 60)
```

---

## Passing Values

| Value |
|-------|
| 18 |
| 25 |
| 60 |

---

## Failing Values

| Value |
|-------|
| 17 |
| 61 |

---

## Notes

- Both boundary values are included.
- Ideal for age, scores, ratings, and similar bounded numeric data.