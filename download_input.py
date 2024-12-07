# https://github.com/gahjelle/template-aoc-python/blob/77ee24e6b80ea99c2a47bdf53d1c46887150db59/src/download_input.py

"""Download input for one Advent of Code puzzle if possible

Uses https://pypi.org/project/advent-of-code-data/ if it's available.
Otherwise, does nothing.
"""

# Standard library imports
import pathlib
import time
import os

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
    year_path = pathlib.Path(__file__).parent / "src" / str(year)
    output_path = next(year_path.glob(f"day{day}")) / "input.txt"
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

if __name__ == "__main__":
    # Read year and day from file structure
    for root, dirs, files in os.walk(__file__ + "/../src"):
        path = root.split(os.sep)
        for directory in dirs:
            if "day" in directory:
                day = int(directory.split("day")[1])
                year = int(path[-1])
                download(year, day)
                print(f"Downloaded input for {year} day {day}")
                time.sleep(1)
print("downloaded all inputs for repository")