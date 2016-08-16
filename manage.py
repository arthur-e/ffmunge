import argparse
import os
import pandas as pd
import re
import sys

VARIABLE_FILENAME = re.compile(r'.*_(?P<id>[HP]{1}[0-9]{3})\.txt$')
TABLE_FILENAME = re.compile(r'^(?P<base>.*)_(?P<id>[HP]{1}[0-9]{3})(_with_ann)?\.csv$')

def list_variables(path):
    '''
    Lists the American FactFinder variables found in the given directory
    <path> based on the metadata files present.
    '''
    assert os.path.exists(path), 'Directory does not exist'
    for filename in os.listdir(path):
        fname_match = VARIABLE_FILENAME.match(filename)
        if fname_match is not None:
            with open(os.path.join(path, filename), 'r') as stream:
                src = stream.readlines(0)
                sys.stdout.write('[%s] %s\n' % tuple(map(str.strip, (src[0], src[1]))))


def merge(path):
    '''
    Merges all of the American FactFinder tables found in the given directory
    <path> into a single table.
    '''
    def read_name_from_metadata(filename_match):
        metadata_fname = ''.join((filename_match.groupdict()['base'], '_',
            filename_match.groupdict()['id'], '.txt'))
        with open(os.path.join(path, metadata_fname)) as stream:
            return stream.readlines(0)[1].strip()

    assert os.path.exists(path), 'Directory does not exist'
    tables = list()
    field_names = ('id', 'fips', 'geog', 'value')
    for filename in os.listdir(path):
        fname_match = TABLE_FILENAME.match(filename)
        if fname_match is not None:
            table = pd.read_csv(os.path.join(path, filename),
                header=[0,1]) # Header on 2 lines
            var_name = read_name_from_metadata(fname_match)
            sys.stdout.write('%s\n' % var_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Commands
    commands_group = parser.add_mutually_exclusive_group()
    commands_group.add_argument('-l', '--list-variables',
        help='List the FactFinder variables found in this directory')
    commands_group.add_argument('-m', '--merge')

    args = parser.parse_args()
    if args.list_variables:
        list_variables(args.list_variables)

    elif args.merge:
        merge(args.merge)
