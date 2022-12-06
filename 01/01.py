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


def generate_bags(data):
    """Generates bags for calories estimation.

    Parameters
    ----------
    data : list
        Unparsed list used to generate Elves bags.

    Returns
    -------
    bags : list
        A list of bags containing calories per elf.
    """

    n_elves = data.count('') + 1

    # Generate bags
    bags = []
    index = 0

    for elf in range(n_elves):
        elf_bag = []

        for i in range(index, len(data)):
            index += 1
            
            if data[i] != '':
                elf_bag.append(int(data[i]))
            else:
                break

        bags.append(elf_bag)

    return bags


def calculate_calories(bags):
    """Calculates the calories per bag.

    Returns the max bag and number of calories.

    Parameters
    ----------
    bags : list
        A list of bags containing calories per elf.

    Returns
    -------
    calories : int
        The max sum of carried calories.
    """

    calories_bags = [sum(bag) for bag in bags]
    calories =  max(calories_bags)

    return calories


def calculate_top_three_calories(bags):
    """Returns the top 3 calories from bags.

    Parameters
    ----------
    bags : list
        A list of bags containing calories per elf.

    Returns
    -------
    calories : int
        Sum of the top 3 list with most calories carried.
    """

    calories_bags = sorted([sum(bag) for bag in bags], reverse=True)
    calories = sum(calories_bags[:3])

    return calories




if __name__ == '__main__':
    parser = cli_parser()
    args = parser.parse_args()

    data = read_input(args.filename)
    bags = generate_bags(data)
    calories = calculate_calories(bags)

    print('The max number of calories carried:', calories)

    top_calories = calculate_top_three_calories(bags)

    print('The sum of top three calories carried:', top_calories)



