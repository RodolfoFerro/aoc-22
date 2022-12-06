# Advent of Code 2022

I'm joining the mini challenges for the Advent of Code this year. You can find more info [here](https://adventofcode.com/2022).

My solutions are implemented in pure Python, using some modukles from the _stdlib_.


### Running the solutions

I created the `main.py` script, which can run any other script with the corresponding solution for each of the days. Each folder contains the corresponding tesing data and input data to solve the challenge and the functions are in the corresponding script (`day/day.py`).

To run the solution of a day, using the example data input simply run the following:

```sh
python main.py -d <day> -f test_input
```

As you can see, the script already uses the relative path to the input data.

To use run the solution of a day with the input data (to solve the challenge), simply change `test_input` with `input` in the terminal. For example, to run the solutions with the data from day 1:

```sh
python main.py -d 1 -f input
```

This should return the following:

```sh
The max number of calories carried: 64929
The sum of top three calories carried: 193697
```

Contact:
- Twitter: [@rodo_ferro](https://twitter.com/rodo_ferro)
- Instagram: [@rodo_ferro](https://instagram.com/rodo_ferro)

