print("Hello, World!")
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
"""
0-99
right - higher
left - lower
starts at 50

number of times left pointing at 0
"""


with open(f"{dir_path}/inputs/day1.txt", "r") as f:
    data = f.readlines()

print(data)

instructions = []
for instruction in data:
    multiplier = 1
    if instruction[0] == "L":
        multiplier = -1

    instructions.append(int(instruction.strip()[1:]) * multiplier)


print(instructions)


position = 50
count = 0

for instruction in instructions:
    position += instruction
    position = position % 100

    if position == 0:
        count += 1

print(count)
