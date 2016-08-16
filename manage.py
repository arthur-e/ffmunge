from core import *

def extract(path, sep=',', quotechar='"', index=False):
    '''
    Extracts a single variable as a table for CSV output; result must be
    piped into a file.
    '''
    assert os.path.exists(path), 'Directory does not exist'
    sys.stdout.write(variable_as_table(path).to_csv(None, sep=sep,
        index=index, quotechar=quotechar))


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



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command-line tool for munging American FactFinder tables')

    # Commands
    commands_group = parser.add_mutually_exclusive_group()
    commands_group.add_argument('-l', '--list-variables', metavar='PATH',
        help='list the FactFinder variables found in this directory')
    commands_group.add_argument('-e', '--extract', metavar='CSV',
        help='extract a table as a formatted CSV, to pipe into a file')

    args = parser.parse_args()
    if args.list_variables:
        list_variables(args.list_variables)

    if args.extract:
        extract(args.extract, args.derivative)
