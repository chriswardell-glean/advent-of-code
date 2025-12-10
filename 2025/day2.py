# comma separated
# separated by -
# IDs are numbers between them
# repeated sequence is invalid of any length of characters
# ignore leading zeroes
# add all invalid IDs up

import os

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

    if id_len % 2 == 0:
        halfway = int(id_len / 2)
        if id_str[0:halfway] == id_str[halfway:]:
            print("HIT", id_str)
            total_sum += id

print(total_sum)
