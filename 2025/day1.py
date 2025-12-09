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
    clicks = 0
    old_position = position
    remainder = abs(instruction) % 100
    full_turns = int((abs(instruction) - remainder) / 100)
    extra_click = 0

    multiplier = -1 if instruction < 0 else 1

    remaining_turn_instruction = remainder * multiplier

    position += remaining_turn_instruction

    # -99 <= remaining_turn_instruction <= 99
    # skip if nothing to move
    # skip if starting at zero, impossible to go past or land on zero
    # only add click if go past zero
    if remaining_turn_instruction != 0 and old_position != 0 and (position <= 0 or position > 99):
        extra_click = 1

    # sanitise for next run to be between 0 and 99
    position = position % 100
    clicks += full_turns + extra_click

    print(instruction, old_position, position, full_turns, extra_click)
    count += clicks

print(count)
