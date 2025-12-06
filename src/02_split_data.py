import click
import pandas as pd
from sklearn.model_selection import train_test_split

@click.command()
@click.option('--input-file', default='src/objects/diabetes_binary_health_indicators_BRFSS2015.csv', help='Input CSV file')

def main(input_file):
    """Split data into train and test sets"""

    dat = pd.read_csv(input_file)
    train_df, test_df = train_test_split(dat, test_size=0.2, random_state=522)

    # Save as CSV
    train_df.to_csv('src/objects/train_df.csv', index=False)
    test_df.to_csv('src/objects/test_df.csv', index=False)

    click.echo("Ran split")

if __name__ == '__main__':
    main()
