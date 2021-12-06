import sys
import click

sys.path.insert(1, '../../src/data')
from dataset_processing import process_dataset as process_dataset_



@click.command()
@click.argument('df', type=click.Path())
@click.argument('out', type=click.Path())
def process_dataset(df, out):
    print('processing_dataset...')
    process_dataset_(df, out)

if __name__ == '__main__':
    process_dataset()