import pandas as pd
import pointblank as pb

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Data Validation - Check that each column has 100% non-missing values
threshold = 1 

validator = pb.Validate(data=train_df)

for col in train_df.columns:
    validator = validator.col_vals_not_null(columns=str(col), thresholds=threshold)

validation_4 = validator.interrogate()

# Check if validation passed and save data validation results
if validation_4.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation4.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation4.txt', index=False)
