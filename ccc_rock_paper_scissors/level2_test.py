import copy
import fileinput
import os

from level2 import styles_after_two_rounds

level = 2
input_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.in"))
output_file = fileinput.input(os.path.join("input", f"level{level}", f"level{level}_example.out"))

N, M = map(int, input_file.readline().strip().split())
for line_index in range(N):
    input_line = input_file.readline().strip()
    output_line = output_file.readline().strip()
    actual_output = styles_after_two_rounds(copy.deepcopy(input_line), M)
    verdict_message = f"input: {input_line}; expected output: {output_line}"
    if actual_output == output_line:
        verdict_message = "\u2705 " + verdict_message
    else:
        verdict_message = "\u274c " + verdict_message + f"; actual output: {actual_output}"
    print(verdict_message)
