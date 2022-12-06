import argparse


def cli_parser():
    """Parser for CLI params.

    Returns
    ------
    parser : argparse:ArgumentParser
        The parser object.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str)

    return parser


def read_input(filename='input.txt'):
    """Reads input file.

    Parameters
    ----------
    filename : str
        The path to the file to be read.

    Returns
    -------
    data : list
        Unparsed list to generate calories bags.
    """

    with open(filename, 'rt') as in_file:
        data = in_file.readlines()

    # Clean data
    data = [line.rstrip('\n') for line in data]

    return data


def parse_data(data):
    """Parses data into a nice format.

    Parameters
    ----------
    data : list
        The input list of data.

    Returns
    -------
    parsed_data : list
        The parsed data.
    """

    parsed_data = data[0]

    return parsed_data


def seek_index(string, size=4):
    """Seeks the index corresponding to the message.

    Parameters
    ----------
    string : str
        Input string to be processed.
    size : int
        The size of the window mesage.

    Returns
    -------
    index :int
        The index corresponding to the unrepeated package.
    """

    index = size - 1

    for i in range(len(string) - index):
        window = string[i:i + size]
        window = set(window)
        index += 1

        if len(window) < size:
            continue
        else:
            break

    return index


if  __name__ == '__main__':
    parser = cli_parser()
    args = parser.parse_args()

    data = read_input(args.filename)
    parsed_data = parse_data(data)
    size = 4
    index = seek_index(parsed_data, size)

    print(f'The resulting index (for size {size}):', index)

    size = 14
    index_longer = seek_index(parsed_data, size)
    
    print(f'The resulting index (for size {size}):', index_longer)

