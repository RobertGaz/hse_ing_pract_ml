import sys
import click

sys.path.insert(1, '../../src/reports')
from visual_analysis import make_report as make_report_



@click.command()
@click.argument('df', type=click.Path())
def make_report(df):
    print('making_visual_report...')
    make_report_(df)

if __name__ == '__main__':
    make_report()