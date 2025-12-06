import click
from pathlib import Path
from ucimlrepo import fetch_ucirepo

@click.command()

def main():
    """Download CDC Diabetes dataset and save as CSV is data/raw directory."""
    
    cdc_diabetes_health_indicators = fetch_ucirepo(id=891) 
    dat = cdc_diabetes_health_indicators.data.original
    
    output_path = 'src/objects/diabetes_binary_health_indicators_BRFSS2015.csv'
    dat.to_csv(output_path, index=False)

    click.echo("Ran fetch")
    
if __name__ == '__main__':
    main()