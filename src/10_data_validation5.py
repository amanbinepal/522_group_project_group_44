import pandas as pd
import pointblank as pb

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Data Validation - Check correct data types in each column
schema_columns = [(col, "int64") for col in train_df.columns]
schema = pb.Schema(columns=schema_columns)

validation_5 = (
    pb.Validate(data=train_df)
    .col_schema_match(schema=schema)
    .interrogate()
)

# Check if validation passed and save data validation results
if validation_5.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation5.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation5.txt', index=False)
