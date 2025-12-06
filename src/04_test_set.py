import click
import pandas as pd

@click.command()
@click.option('--test-file', default='objects/test_df.csv', help='Test CSV file')

def main(test_file):
    """Split test data into features (X_test) and target (y_test)"""
    
    test_df = pd.read_csv(test_file)
    
    X_test, y_test = (
        test_df.drop(columns=["Diabetes_binary"]),
        test_df["Diabetes_binary"],
    )
    
    # Save as CSV
    X_test.to_csv('objects/X_test.csv', index=False)
    y_test.to_csv('objects/y_test.csv', index=False)
    
if __name__ == '__main__':
    main()
