import argparse
import os


def build_parser():
    """Builds parser for CLI params.

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser object.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', type=int, default=1)
    parser.add_argument('-f', '--filename', type=str, default='test_input')
    parser.add_argument('-r', '--relative-route', type=bool, default=True)

    return parser


def main():
    """Runs the solution of each day."""

    parser = build_parser()
    args = parser.parse_args()

    day = args.day
    filename = args.filename
    relative_route = args.relative_route
    day_path = os.path.join(f'{day:02d}')

    if relative_route:
        filename = os.path.join(day_path, filename)

    os.system(f'python {day_path}/{day:02d}.py -f {filename}')



if __name__ == '__main__':
    main()

