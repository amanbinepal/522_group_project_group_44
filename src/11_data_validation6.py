import pandas as pd
import pointblank as pb

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Data Validation - Check for no duplicate observations
unique_key_cols = ["ID"]  # use only the primary key column "ID" 

validation_6 = (
    pb.Validate(data=train_df)
    .rows_distinct(columns_subset=unique_key_cols)
    .interrogate()
)

# Check if validation passed and save data validation results
if validation_6.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation6.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation6.txt', index=False)
    print("Warning: Duplicate observations detected")
