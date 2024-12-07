# https://github.com/AlexeSimon/adventofcode/blob/master/init.py
# https://github.com/gahjelle/template-aoc-python/blob/main/src/download_input.py

"""Download input for one Advent of Code puzzle if possible

Uses https://pypi.org/project/advent-of-code-data/ if it's available.
Otherwise, does nothing.
"""

# Standard library imports
import pathlib
import sys

# Third party imports
try:
    from aocd.models import Puzzle
except ImportError:
    pypi_url = "https://pypi.org/project/advent-of-code-data/"
    print(f"Install {pypi_url} to autodownload input files")
    raise SystemExit()


def download(year, day):
    """Get input and write it to input.txt inside the puzzle folder"""
    puzzle = Puzzle(year=year, day=day)

    # Download input
    try:
        year_path = pathlib.Path(__file__).parent / str(year)
        output_path = f"{year_path.glob(f'{day:02d}*')} / input.txt"
        output_path.write_text(puzzle.input_data)

        # Download example data
        for index, example in enumerate(puzzle.examples, start=1):
            output_path = output_path.with_stem(f"example{index}")
            output_path.write_text(example.input_data)

        # Add README with link to puzzle text
        readme_path = output_path.with_name("README.md")
        readme_path.write_text(
            f"# {puzzle.title}\n\n"
            f"**Advent of Code: Day {day}, {year}**\n\n"
            f"See {puzzle.url}\n"
        )
    except StopIteration:
        print(f"No puzzle found for day {day} in year {year}")

# echo AOC_SESSION="SESSION_ID" > .env on windows powershell

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Missing year")
            raise SystemExit()

        # Read year and day from command line
        for day in range(0, 31):
            # download(year=int(sys.argv[1]), day=day)
            download(year=2024, day=day)
    except Exception as err:
        # Catch exceptions so that Copier doesn't clean up directories
        print(f"Download of input failed: {err}")
        raise SystemExit()