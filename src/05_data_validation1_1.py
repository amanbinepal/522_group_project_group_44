import pandas as pd
import pointblank as pb

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Data Validation - Check column count
validation_1_1 = (
    pb.Validate(data=train_df)
    .col_count_match(len(train_df.columns))
    .interrogate()
)

# Check if validation passed and save data validation results
if validation_1_1.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation1_1.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation1_1.txt', index=False)
