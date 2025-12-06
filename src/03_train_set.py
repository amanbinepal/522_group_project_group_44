import click
import pandas as pd

@click.command()
@click.option('--train-file', default='objects/train_df.csv', help='Training dataset CSV file')

def main(train_file):
    """Split training data into features (X_train) and target (y_train)"""
    
    train_df = pd.read_csv(train_file)
    
    X_train, y_train = (
        train_df.drop(columns=["Diabetes_binary"]),
        train_df["Diabetes_binary"],
    )
    
    # Save as CSV
    X_train.to_csv('objects/X_train.csv', index=False)
    y_train.to_csv('objects/y_train.csv', index=False)

if __name__ == '__main__':
    main()
