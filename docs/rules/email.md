# Email

The `email()` rule validates email addresses.

---

## Syntax

```python
validator.column("email").email()
```

---

## Example

```python
validator.column("email") \
    .required() \
    .email()
```

---

## Passing Values

| Value |
|-------|
| john@example.com |
| alice@gmail.com |

---

## Failing Values

| Value |
|-------|
| johngmail.com |
| hello@ |
| @gmail.com |

---

## Notes

- Should usually be combined with `required()`.