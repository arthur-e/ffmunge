import argparse
import os
import pandas as pd
import re
import sys

VARIABLE_FILENAME = re.compile(r'.*_(?P<id>[HP]{1}[0-9]{3})\.txt$')
TABLE_FILENAME = re.compile(r'^(?P<base>.*)_(?P<id>[HP]{1}[0-9]{3})(_with_ann)?\.csv$')

def variable_as_table(path, with_geography=True):
    '''
    Formats a variable, stored in a CSV file, as a Pandas table.
    '''
    if with_geography:
        return pd.read_csv(path, skiprows=[0]).rename(columns={
            'Id': 'id',
            'Id2': 'fips',
        }).drop('Geography', axis=1, errors='ignore')

    else:
        raise NotImplementedError('Nothing for with_geography=False')
