import sys
import click

sys.path.insert(1, '../../src/data')
from raw_csv_processing import process_raw_csv as process_raw_csv_



@click.command()
@click.argument('df1', type=click.Path())
@click.argument('df2', type=click.Path())
@click.argument('out', type=click.Path())
def process_raw_csv(df1, df2, out):
    print('processing_raw_csv...')
    process_raw_csv_(df1, df2, out)

if __name__ == '__main__':
    process_raw_csv()