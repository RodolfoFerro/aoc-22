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
        The list converted to consistend symbology.
    """

    # Split symbols
    parsed_data = []

    for line in data:
        range_1, range_2 = line.split(',')
        low_a, high_a = range_1.split('-')
        low_b, high_b = range_2.split('-')
        set_a = set(range(int(low_a), int(high_a) + 1))
        set_b = set(range(int(low_b), int(high_b) + 1))

        parsed_data.append((set_a, set_b))

    return parsed_data


def count_contained(parsed_data):
    """Counts contained subsets.

    Parameters
    ----------
    parsed_data : list
        A list containing pairs of sets to be used.

    Returns
    -------
    contained : int
        The number of contained subsets.
    """

    contained = 0

    for (set_a, set_b) in parsed_data:
        if set_a <= set_b or set_b <= set_a:
            contained += 1

    return contained


def count_intersections(parsed_data):
    """Counts contained subsets.

    Parameters
    ----------
    parsed_data : list
        A list containing pairs of sets to be used.

    Returns
    -------
    intersections : int
        The number of intersections.
    """

    intersections = 0

    for (set_a, set_b) in parsed_data:
        if len(set_a.intersection(set_b)) > 0:
            intersections += 1

    return intersections


if  __name__ == '__main__':
    parser = cli_parser()
    args = parser.parse_args()

    data = read_input(args.filename)
    parsed_data = parse_data(data)
    contained = count_contained(parsed_data)
    
    print('The number of contained subsets:', contained)

    intersections = count_intersections(parsed_data)

    print('The number of intersections:', intersections)

