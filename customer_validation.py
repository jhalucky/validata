import pandas as pd
from veris import Validator

df = pd.read_csv("customers.csv")

validator = Validator(df)

validator.column("customer_id").required().unique()
validator.column("name").required().min_length(3).max_length(30)
validator.column("email").required().email()
validator.column("age").between(18,60)
validator.column("salary").minimum(0)

result = validator.validate()

print(result.passed)
result.report()