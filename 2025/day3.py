import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{dir_path}/inputs/day3.txt", "r") as f:
    banks = f.read().splitlines()


# turn on only 2 batteries in each bank
# concat numbers to get voltage
# sum joltages

total_joltage = 0

number_of_batteries = 12

for bank in banks:
    batteries = list(bank)
    batteries_enabled = ""

    start_index = 0

    for iteration in range(0, number_of_batteries):
        end_index_count = number_of_batteries - iteration - 1
        # if 0, then we can go to end of list
        end_index = None if end_index_count == 0 else end_index_count * -1

        sub_bank = batteries[start_index:end_index]
        print(bank, iteration, start_index, sub_bank)
        highest_first_number = max(sub_bank)
        start_index = start_index + sub_bank.index(highest_first_number) + 1

        batteries_enabled += highest_first_number
        print(highest_first_number, start_index)
    total_joltage += int(batteries_enabled)

print(total_joltage)
