# python solution.py input.txt

import pathlib
import sys
from typing import Any, TypeVar

# Type annotation alias
T = TypeVar('tuple[list[int], list[list[list[int]]]]') # type: ignore


def intify(list_of_strings: list[str]) -> list[int]:
  """ Convert a list of strings into one of ints """
  return [int(c) for c in list_of_strings]


def format_board(board: list[str]) -> list[int]:
  """ Format each board from the input into int equivalents """
  formatted_board = []
  for row in board.splitlines():
    row = row.replace('  ', ' ')
    formatted_board.append(row.split())
  return [intify(board) for board in formatted_board]


def parse(puzzle_input: str) -> T:
  """ Parse input """
  data = puzzle_input.split('\n\n')
  nums, boards = data[0].split(','), data[1:]
  return (intify(nums), [format_board(board) for board in boards])


def invert_board(board: list[list[int]]) -> list[list[int]]:
  """ Switch rows and columns of board """
  return [list(tupp) for tupp in list(zip(*board))]


def winning_turns(nums: list[int], seq: list) -> int:
  """ Return num of times it takes to match all nums in a sequence """
  counter, turns = 0, 0
  for num in nums:
    turns += 1
    if num in seq:
      counter += 1
      if counter == 5:
        return turns


def get_scores(board: list[list[int]], nums: list[int]) -> list[int]:
    """ Return a list of winning turns for a board """
    return [winning_turns(nums, seq) for seq in board]


def scores(board: list[list[int]], nums: list[int]) -> list[int]:
  """ Calculate scores for board and return all values as a list """
  results = []
  by_row = get_scores(board, nums)
  by_col = get_scores(invert_board(board), nums)
  for row, col in zip(by_row, by_col):
    results.append(min(row, col))
  return results


def board_scores(boards: T, nums: list[int]) -> dict[int, list[int]]:
  """ Get all the quickest scores for each board """
  return {
    board_no: min(scores(board, nums))
    for board_no, board in enumerate(boards)
  }


def flatten(t: list[list[Any]]) -> list[Any]:
  """ Flatten a nested list """
  return [item for sublist in t for item in sublist]


def final_score(board: list[list[int]], played_nums: list[int]) -> int:
  """ Work out final score using sets """
  last_num = played_nums[-1]
  board_nums = set(flatten(board))
  remaining_numbers = board_nums - set(played_nums)
  return sum(remaining_numbers) * last_num


def part1(data: T) -> int:
  """ Solve part 1 """
  nums, boards = data[0], data[1]
  board_info = board_scores(boards, nums)
  # Get quickest board
  quickest = min(board_info, key=board_info.get)
  num_turns = board_info[quickest]
  return final_score(boards[quickest], nums[:num_turns])


def part2(data: T) -> int:
  """ Solve part 2 """
  nums, boards = data[0], data[1]
  board_info = board_scores(boards, nums)
  # Get slowest board
  slowest = max(board_info, key=board_info.get)
  num_turns = board_info[slowest]
  return final_score(boards[slowest], nums[:num_turns])


def solve(puzzle_input: T) -> tuple[int, int]:
  """ Solve the puzzle for the given input """
  data = parse(puzzle_input)
  solution1 = part1(data)  # Correct answer was 58412 (with my data)
  solution2 = part2(data)  # Correct answer was 10030 (with my data)

  return solution1, solution2


if __name__ == "__main__":
  for path in sys.argv[1:]:
    print(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))