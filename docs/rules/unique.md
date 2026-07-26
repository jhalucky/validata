# Unique

The `unique()` rule ensures that all values in a column are unique.

---

## Syntax

```python
validator.column("customer_id").unique()
```

---

## Example

```python
validator.column("customer_id") \
    .required() \
    .unique()
```

---

## Passing Values

| Values |
|---------|
| 1,2,3,4 |

---

## Failing Values

| Values |
|---------|
| 1,2,2,4 |

---

## Notes

- Useful for primary keys.
- Duplicate rows are reported.