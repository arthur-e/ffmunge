import argparse
import os
import re
import sys

def list_variables(path):
    variable_filename = re.compile(r'.*_(?P<id>[HP]{1}[0-9]{3})\.txt$')
    assert os.path.exists(path), 'Directory does not exist'
    for filename in os.listdir(path):
        fname_match = variable_filename.match(filename)
        if fname_match is not None:
            with open(os.path.join(path, filename), 'r') as stream:
                src = stream.readlines(0)
                sys.stdout.write('[%s] %s\n' % tuple(map(str.strip, (src[0], src[1]))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Commands
    commands_group = parser.add_mutually_exclusive_group()
    commands_group.add_argument('-l', '--list-variables',
        help='List the FactFinder variables found in this directory')

    args = parser.parse_args()
    if args.list_variables:
        list_variables(args.list_variables)
