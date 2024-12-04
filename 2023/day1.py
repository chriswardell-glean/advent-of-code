import re

def reverse_str(input: str) -> str:
    input_list = list(input)
    input_list.reverse()
    return "".join(input_list)

def convert_to_number(input: str, reversed = False):
    if len(input) == 1:
        return input

    if reversed:
        input = reverse_str(input)

    lookup_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    return lookup_dict[input]


def get_first_digit_in_str(input: str, reversed = False) -> str:
    if reversed:
        pattern = re.compile("(1|2|3|4|5|6|7|8|9|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)")
    else:
        pattern = re.compile("(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)")

    matches = re.search(pattern, input)
    first_match = matches.group(1)
    return convert_to_number(first_match, reversed=reversed)


def get_last_digit_in_str(input: str) -> str:
    return get_first_digit_in_str(reverse_str(input), reversed=True)




raw_calibration_values = []

with open("./inputs/day1.txt") as f:
    raw_calibration_values = f.read().split("\n")

total = 0

for value in raw_calibration_values:
    try:
        first_digit = get_first_digit_in_str(value)
        last_digit = get_last_digit_in_str(value)
    except:
        print("Uh oh", value)
    total += int(first_digit+last_digit)
    
print(total)