import argparse
import re


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


def parse_data(data, convert=True):
    """Parses data into a nice format.

    Parameters
    ----------
    data : list
        The input list of data.
    convert : bool
        A flag to specify if data needs to be converted.

    Returns
    -------
    parsed_data : list
        The list converted to consistend symbology.
    """

    # Substitute symbols
    if convert:
        converted_data = [re.sub('X', 'A', line) for line in data]
        converted_data = [re.sub('Y', 'B', line) for line in converted_data]
        converted_data = [re.sub('Z', 'C', line) for line in converted_data]
    
        # Convert to numbers
        v_data = [line.split(' ') for line in converted_data]
        v_data = [[int(ord(item[0]) - 65), int(ord(item[1]) - 65)] for item in v_data]
    else:
        # Convert to numbers
        v_data = [line.split(' ') for line in data]
        v_data = [[int(ord(item[0]) - 65), int(ord(item[1]) - 89)] for item in v_data]

    parsed_data = v_data

    return parsed_data


def results_per_round(parsed_data, converted=True):
    """Computes the results per round.

    Parameters
    ----------
    parsed_data : list
        A list containing a lists of pairs of selections.
    converted : bool
        A flag to specify if data was converted or taken as raw.

    Returns
    -------
    results : list
        A list with the results per round.
    """

    results = []

    # Process converted results
    if converted:
        for (their_hand, my_hand) in parsed_data:
            result = my_hand - their_hand
        
            if result == 0:
                # Report tie
                results.append([my_hand + 1, 3])
            elif result in [1, -2]:
                # Report win
                results.append([my_hand + 1, 6])
            elif result in [2, -1]:
                # Report loss
                results.append([my_hand + 1, 0])
    else:
        for (hand, expectation) in parsed_data:
            if expectation == 0:
                # Report tie
                results.append([hand + 1, 3])
            if expectation == -1:
                # Report loss
                my_hand = (hand - 1) % 3
                results.append([my_hand + 1, 0])
            if expectation == 1:
                # Report win
                my_hand = (hand + 1) % 3
                results.append([my_hand + 1, 6])

    return results


def compute_score(results):
    """Returns the resulting score of rounds.

    Parameters
    ----------
    results : list
        The results per round.

    Returns
    -------
    score : int
        The final score.
    """

    scores = []
    for (fig, round_score) in results:
        scores.append(fig + round_score)

    score = sum(scores)

    return score


if  __name__ == '__main__':
    parser = cli_parser()
    args = parser.parse_args()

    data = read_input(args.filename)
    parsed_data_converted = parse_data(data)
    results = results_per_round(parsed_data_converted)
    score = compute_score(results)

    print('The score of all rounds:', score)

    parsed_data = parse_data(data, convert=False)
    expected_results = results_per_round(parsed_data, converted=False)
    score_expected = compute_score(expected_results)

    print('The expected score of all rounds:', score_expected)

