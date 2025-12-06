import pandas as pd
from deepchecks.tabular import Dataset, Suite
from deepchecks.tabular.checks import ClassImbalance, FeatureLabelCorrelation, FeatureFeatureCorrelation

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Define binary features (excluding the label 'Diabetes_binary')
binary_features = ['HighBP', 'HighChol', 'CholCheck', 'Smoker', 
                   'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits',
                   'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost',
                   'DiffWalk', 'Sex']

# Create deepchecks Dataset
deep_train = Dataset(train_df.drop(columns=['ID']),
                     label="Diabetes_binary",
                     cat_features=binary_features)

# Data Validation - Check for class imbalance and correlations
suite = Suite(
    "Validation",
    ClassImbalance(),
    FeatureLabelCorrelation(correlation_threshold=0.5),
    FeatureFeatureCorrelation(correlation_threshold=0.7),
)

suite_result = suite.run(deep_train)

# Check if validation passed and save data validation results
if suite_result.passed():
    pd.DataFrame({'result': ['PASS']}).to_csv('objects/pass_data_validation10.txt', index=False)

else:
    pd.DataFrame({'result': ['FAILED']}).to_csv('objects/failed_data_validation10.txt', index=False)

