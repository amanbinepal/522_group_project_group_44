import pandas as pd
import pointblank as pb

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Data Validation - Check that all rows are complete with no missing values
validation_3 = (
    pb.Validate(data=train_df)
    .rows_complete() 
    .interrogate()
)

# Check if validation passed and save data validation results
if validation_3.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation3.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation3.txt', index=False)
