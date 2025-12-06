import pandas as pd

# Read in the CSV file - from split_data.py script output
train_df = pd.read_csv('objects/train_df.csv')

# Data Validation - Check value ranges for ordinal features
ordinal_features = ["GenHlth", "MentHlth", "PhysHlth", "Age", "Education", "Income"]

for f in ordinal_features: 
    temp_col = train_df[f]
    print(f"========================================== {f}")
    print(f"datatype: {temp_col.dtype}")
    print(temp_col.sort_values().value_counts().index)

#This is an exploratory check for value ranges of ordinal features. No pass/fail output.