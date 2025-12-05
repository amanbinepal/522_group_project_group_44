import pandas as pd
import pointblank as pb

# Read in the CSV files - from split_data.py script output and raw data
train_df = pd.read_csv('objects/train_df.csv')
original_data = pd.read_csv('objects/diabetes_binary_health_indicators_BRFSS2015.csv') 

# Data Validation - Check row count (80% split)
rows, cols = original_data.shape
train_target = int(rows * 0.8)

validation_1_2 = (
    pb.Validate(data=train_df)
    .row_count_match(train_target)
    .interrogate()
)

# Check if validation passed and save data validation results
if validation_1_2.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation2.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation2.txt', index=False)
