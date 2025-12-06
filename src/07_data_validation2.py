import pandas as pd
import pointblank as pb

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Data Validation - Check that data contains all required column names
expected_columns = ['ID', 'Diabetes_binary', 'HighBP', 'HighChol', 'CholCheck', 'BMI',
                   'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits',
                   'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
                   'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age',
                   'Education', 'Income']

validation_2 = (
    pb.Validate(data=train_df)
    .col_exists(columns=expected_columns)
    .interrogate()
)

# Check if validation passed and save data validation results
if validation_2.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation2.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation2.txt', index=False)
