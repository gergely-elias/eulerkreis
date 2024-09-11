import copy
import fileinput
import os

from level4 import first_round_pairing_whole_tourney
from helpers import tourney_winner

level = 4
input_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.in"))
output_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.out"))

N, M = map(int, input_file.readline().strip().split())
for line_index in range(N):
    input_line = input_file.readline().strip()
    output_line = output_file.readline().strip()
    style_counts = {data[-1]: int(data[:-1]) for data in input_line.split()}
    actual_output = first_round_pairing_whole_tourney(copy.deepcopy(style_counts), M)
    verdict_message = f"input: {input_line}; example output: {output_line}"
    actual_tourney_winner = tourney_winner(actual_output, M)
    if all(actual_output.count(style) == style_counts[style] for style in "RPS") and actual_tourney_winner == "S":
        verdict_message = "\u2705 " + verdict_message
    else:
        verdict_message = "\u274c " + verdict_message + f"; actual output: {actual_output}"
    print(verdict_message)
