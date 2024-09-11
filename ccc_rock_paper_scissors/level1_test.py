import copy
import fileinput
import os

from level1 import fight_winner

level = 1
input_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.in"))
output_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.out"))

N = int(input_file.readline().strip())
for line_index in range(N):
    input_line = input_file.readline().strip()
    output_line = output_file.readline().strip()
    actual_output = fight_winner(copy.deepcopy(input_line))
    verdict_message = f"input: {input_line}; expected output: {output_line}"
    if actual_output == output_line:
        verdict_message = "\u2705 " + verdict_message
    else:
        verdict_message = "\u274c " + verdict_message + f"; actual output: {actual_output}"
    print(verdict_message)
