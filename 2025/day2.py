# comma separated
# separated by -
# IDs are numbers between them
# repeated sequence is invalid of any length of characters
# ignore leading zeroes
# add all invalid IDs up

import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{dir_path}/inputs/day2.txt", "r") as f:
    data = f.readlines()

raw_id_ranges = data[0].split(",")

clean_ids = []

for id_range in raw_id_ranges:
    first = int(id_range.split("-")[0])
    second = int(id_range.split("-")[1])

    for id in range(first, second + 1):
        clean_ids.append(id)

total_sum = 0

for id in clean_ids:
    id_str = str(id)
    id_len = len(id_str)
    halfway = math.floor(id_len / 2)

    for pattern_length in range(1, halfway + 1):
        # check if this substring length will fit if repeated
        if id_len % pattern_length == 0:
            number_of_repeats = int(id_len / pattern_length)

            if id_str == id_str[:pattern_length] * number_of_repeats:
                print(pattern_length, id_str, id_str[:pattern_length])
                total_sum += id
                break


print(total_sum)
