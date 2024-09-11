import copy
import fileinput
import os

from level6 import replace_Xs
from helpers import tourney_winner_5

level = 6
input_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.in"))
output_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.out"))

N, M = map(int, input_file.readline().strip().split())
for line_index in range(N):
    input_line = input_file.readline().strip()
    output_line = output_file.readline().strip()
    actual_output = replace_Xs(copy.deepcopy(input_line), M)
    verdict_message = f"input: {input_line}; example output: {output_line}"
    actual_tourney_winner = tourney_winner_5(actual_output, M)
    if all(input_line[style_index] == "X" or input_line[style_index] == actual_output[style_index] for style_index in range(M)) and actual_tourney_winner == "S":
        verdict_message = "\u2705 " + verdict_message
    else:
        verdict_message = "\u274c " + verdict_message + f"; actual output: {actual_output}"
    print(verdict_message)
