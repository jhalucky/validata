# Minimum

The `minimum()` rule ensures that a numeric value is greater than or equal to a specified minimum.

---

## Syntax

```python
validator.column("salary").minimum(0)
```

---

## Example

```python
validator.column("salary") \
    .minimum(0)
```

---

## Passing Values

| Value |
|-------|
| 0 |
| 1000 |

---

## Failing Values

| Value |
|-------|
| -1 |
| -100 |

---

## Notes

- Commonly used for salaries, prices, and quantities.