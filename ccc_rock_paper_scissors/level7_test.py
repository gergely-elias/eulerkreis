import copy
import fileinput
import os

from level7 import replace_Xs_Z
from helpers import tourney_winner_5_Z

level = 7
input_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.in"))
output_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.out"))

N, M = map(int, input_file.readline().strip().split())
for line_index in range(N):
    input_line = input_file.readline().strip()
    output_line = output_file.readline().strip()
    actual_output = replace_Xs_Z(copy.deepcopy(input_line), M)
    # actual_output = copy.deepcopy(output_line)
    verdict_message = f"input: {input_line}; example output: {output_line}"
    actual_tourney_winner = tourney_winner_5_Z(actual_output, M)
    # print("TW", actual_tourney_winner)
    if all(input_line[style_index] == "X" or input_line[style_index] == actual_output[style_index] for style_index in range(M)) and len(actual_tourney_winner) == 1 and "S" in actual_tourney_winner:
        verdict_message = "\u2705 " + verdict_message
    else:
        verdict_message = "\u274c " + verdict_message + f"; actual output: {actual_output}"
    print(verdict_message)
