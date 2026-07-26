# Max Length

The `max_length()` rule ensures that a string does not exceed the specified number of characters.

---

## Syntax

```python
validator.column("name").max_length(30)
```

---

## Example

```python
validator.column("name") \
    .max_length(30)
```

---

## Passing Values

| Value |
|-------|
| Alice |
| Jonathan |

---

## Failing Values

| Value |
|-------|
| ThisIsAnExtremelyLongNameBeyondThirtyCharacters |

---

## Notes

- Useful for enforcing database field limits.