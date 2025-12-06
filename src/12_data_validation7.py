import pandas as pd
import pointblank as pb

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Data Validation - Check for no outliers in BMI (numeric range check)
validation_7 = (
    pb.Validate(data=train_df)
    .col_vals_between(columns="BMI", left=10, right=100)  # BMI is unlikely to go under 10 or exceed 100
    .interrogate()
)

# Check if validation passed and save data validation results
if validation_7.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation7.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation7.txt', index=False)
    print("Warning: Outlier values detected in BMI")
