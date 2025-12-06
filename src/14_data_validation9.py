import pandas as pd
import pointblank as pb

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Define binary features
binary_features = ['Diabetes_binary', 'HighBP', 'HighChol', 'CholCheck', 'Smoker', 
                   'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits',
                   'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
                   'DiffWalk', 'Sex']

# Data Validation - Check correct category levels for categorical/ordinal features
validation_9 = (
    pb.Validate(data=train_df)
    .col_vals_in_set(columns=binary_features, set=[0, 1])  # binary features: 0/1
    .col_vals_in_set(columns="GenHlth", set=list(range(1, 6)))  # scale of 1-5
    .col_vals_between(columns=["MentHlth", "PhysHlth"], left=0, right=30)  # number of days out of 30 days
    .col_vals_in_set(columns="Age", set=list(range(1, 14)))  # scale of 1-13
    .col_vals_in_set(columns="Education", set=list(range(1, 7)))  # scale of 1-6
    .col_vals_in_set(columns="Income", set=list(range(1, 9)))  # scale of 1-8
    .interrogate()
)

# Check if validation passed and save data validation results
if validation_9.all_passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation9.txt', index=False)
else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation9.txt', index=False)
    print("Warning: Incorrect category levels detected")
