# Getting Started

Welcome to **Veris**.

Veris is a lightweight, fluent, and extensible data validation library for Python. It helps you define validation rules for tabular data and generate clear, easy-to-read validation reports.

Whether you're validating CSV files, Pandas DataFrames, or other structured datasets, Veris provides a simple API that is easy to learn and scales as your projects grow.

---

## Why Veris?

Data validation is an essential step in every data pipeline. Missing values, duplicate records, invalid emails, or unexpected data types can lead to unreliable analysis and downstream failures.

Veris makes it easy to detect these issues before they become problems.

### Clean & Fluent API

```python
validator.column("email") \
    .required() \
    .email()

validator.column("age") \
    .between(18, 60)
```

The fluent interface keeps validation rules readable and easy to maintain.

---

## Supported Data Sources

Veris currently supports:

- Pandas DataFrames

Future releases will include support for:

- Polars DataFrames
- PySpark DataFrames
- CSV files
- Excel files
- Parquet files
- SQL query results

---

## Core Concepts

Veris is built around four simple concepts.

### 1. Create a Validator

The `Validator` is the entry point for every validation.

```python
validator = Validator(df)
```

---

### 2. Select a Column

Choose the column you want to validate.

```python
validator.column("email")
```

---

### 3. Add Validation Rules

Attach one or more validation rules to the selected column.

```python
validator.column("email") \
    .required() \
    .email()
```

Rules can be chained together to create expressive validation logic.

---

### 4. Run Validation

Execute all configured rules.

```python
result = validator.validate()
```

If any rules fail, Veris collects all validation errors into a single result.

---

## View the Report

Display a summary of the validation results.

```python
result.report()
```

Example:

```text
**************************************************
                VERIS REPORT
**************************************************

Status      : FAILED
Total Errors: 3

--------------------------------------------------
Column      : email
Rule        : email
Failed Rows : [5, 12]

--------------------------------------------------
Column      : age
Rule        : between
Failed Rows : [8]
```

---

## Philosophy

Veris is designed around a few core principles:

- **Simple** – Easy to learn and use.
- **Readable** – Validation code should be self-explanatory.
- **Extensible** – New validation rules can be added without changing existing code.
- **Framework Agnostic** – Works alongside your existing data workflows.
- **Developer Friendly** – Clear error reporting and predictable behaviour.

---

## What's Next?

Now that you're familiar with the basic concepts, continue with:

- **Installation** – Learn how to install Veris.
- **Quick Start** – Build your first validator in a few minutes.
- **Validator** – Explore the complete Validator API.
- **Rules** – Learn about every built-in validation rule.