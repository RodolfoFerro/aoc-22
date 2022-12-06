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
        n_chars = len(line) // 2
        parsed_data.append([line[:n_chars], line[n_chars:]])

    return parsed_data


def find_repeated(parsed_data):
    """Finds the repeated item per package.

    Parameters
    ----------
    parsed_data : list
        A list containing splited packages.

    Returns
    -------
    reps : list
        The list with repeated elements in packages.
    """

    reps = []

    for (pkg_a, pkg_b) in parsed_data:
        for item in pkg_a:
            if item in pkg_b:
                reps.append(item)
                break

    return reps


def calculate_priorities(repeated_values):
    """Calculates the sum of priority values of repeated items.

    Parameters
    ----------
    repeated_values : list
        List of repeated values.

    Returns
    -------
    score : int
        The sum of priority values of repeated items.
    """

    scores = []

    for item in repeated_values:
        value = ord(item)

        if value > 96:
            value -= 96
        else:
            value -= 38

        scores.append(value)

    score = sum(scores)

    return score


def find_common_between_three(data):
    """Finds common item each 3 rucksacks.

    Parameters
    ----------
    data : list
        The input list of data.

    Returns
    -------
    reps : list
        The list with repeated items each 3 sacks.
    """

    n_triplets = len(data) // 3
    reps = []
    
    for i in range(n_triplets):
        pack_1 = data[3 * i]
        pack_2 = data[3 * i + 1]
        pack_3 = data[3 * i + 2]

        for item in pack_1:
            if item in pack_2 and item in pack_3:
                reps.append(item)
                break

    return reps



if  __name__ == '__main__':
    parser = cli_parser()
    args = parser.parse_args()

    data = read_input(args.filename)
    parsed_data = parse_data(data)
    reps = find_repeated(parsed_data)
    score = calculate_priorities(reps)
    
    print('The sum of priorities:', score)

    reps_each_three = find_common_between_three(data)
    scores_three = calculate_priorities(reps_each_three)

    print('The sum of priorities each three:', scores_three)


