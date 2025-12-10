import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{dir_path}/inputs/day3.txt", "r") as f:
    banks = f.read().splitlines()


# turn on only 2 batteries in each bank
# concat numbers to get voltage
# sum joltages

total_joltage = 0

for bank in banks:
    batteries = list(bank)
    # first number can't be the last number, must be two batteries!
    highest_first_number = max(batteries[:-1])
    # leftmost index of the highest first number means we can have more available second numbers to get a higher number with
    index_of_first_number = batteries.index(highest_first_number)

    highest_second_number = max(batteries[index_of_first_number + 1 :])

    total_joltage += int(highest_first_number + highest_second_number)

print(total_joltage)
