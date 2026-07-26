
---

# 3. quickstart.md

This is probably the most important page.

```md
# Quick Start

Create a Validator.

```python
validator = Validator(df)
```

Validate a column.

```python
validator.column("email") \
    .required() \
    .email()
```

Validate another column.

```python
validator.column("age") \
    .between(18, 60)
```

Run validation.

```python
result = validator.validate()

result.report()
```

Done.
```

---

