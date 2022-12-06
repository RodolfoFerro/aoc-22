import argparse
import copy
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


def parse_data(data):
    """Parses data into a nice format.

    Parameters
    ----------
    data : list
        The input list of data.

    Returns
    -------
    stacked_data : list
        The list of stacks with data.
    movements : list
        The list of movements for each stack.
    """

    # Split symbols
    parsed_data = []
    highest_tile = 0

    # Read number pf stacks to be used
    for line in data:
        if not line.startswith(' 1'):
            highest_tile += 1
        else:
            n_stacks = line[1:-1].split('   ')
            break

    # Parse lines
    parsed_data = []

    for i in range(highest_tile - 1, -1, -1):
        line = re.sub('    ', ' ', data[i])
        line = line.split(' ')
        parsed_data.append(line)

    # Build stacks
    stacked_data = []

    for line in parsed_data:
        for i in range(len(line)):
            if line[i] != '':
                if len(stacked_data) < i + 1:
                    stacked_data.append([])
                stacked_data[i].append(line[i])

    # Build movements
    movements = []

    for i in range(highest_tile + 2, len(data)):
        line = re.sub('move ', '', data[i])
        line = re.sub(' from ', ' ', line)
        line = re.sub(' to ', ' ', line)
        line = line.split(' ')
        line = [int(item) for item in line]

        movements.append(line)

    return stacked_data, movements


def apply_movements(stacked_data, movements, inplace=False):
    """Applies movements between stacks.

    Parameters
    ----------
    stacked_data : list
        The list of stacks.
    movements : list
        The movements in format (number, from, to).

    Returns
    -------
    resulting_stacks : list
        The resulting list of stacks after movements.
    """

    resulting_stacks = copy.deepcopy(stacked_data)

    if not inplace:
        for movement in movements:
            n_moves, from_, to_ = movement

            for i in range(n_moves):
                item = resulting_stacks[from_ - 1].pop()
                resulting_stacks[to_ - 1].append(item)
    else:
        for movement in movements:
            n_moves, from_, to_ = movement

            items = resulting_stacks[from_ - 1][-n_moves:]
            resulting_stacks[to_ - 1] += items

            for item in items:
                resulting_stacks[from_ -1].pop()

    return resulting_stacks


def plot_stacks(stacks):
    """Prints stacks in console.

    Parameters
    ----------
    stacks : list
        The list of stacks to be displayed.
    """
    
    highest_top = max([len(stack) for stack in stacks])
    
    lines = []

    for i in range(highest_top):
        line = ''
        for stack in stacks:
            if i < len(stack):
                line += stack[i]
            else:
                line += '   '
        lines.insert(0, line)

    for line in lines:
        print(line)


def return_tops(stacks):
    """Returns the top items of each stack.

    Parameters
    ----------
    stacks : list
        The list of stacks to be used.

    Returns
    -------
    tops : str
        A string with the tops of all stacks.
    """
    
    tops = ''

    for stack in stacks:
        tops += stack[-1][1:-1]

    return tops


if  __name__ == '__main__':
    parser = cli_parser()
    args = parser.parse_args()

    data = read_input(args.filename)
    stacked_data, movements = parse_data(data)
    resulting_stacks = apply_movements(stacked_data, movements)
    tops = return_tops(resulting_stacks)

    plot_stacks(resulting_stacks)
    print('The final tops of stacks:', tops)
    print()

    resulting_stacks_inplace = apply_movements(stacked_data, movements, inplace=True)
    tops_inplace = return_tops(resulting_stacks_inplace)

    plot_stacks(resulting_stacks_inplace)
    print('The final tops of stacks (inplace):', tops_inplace)


