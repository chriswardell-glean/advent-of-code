import math

def get_numbers_from_list(numbers_list):
    numbers = []
    for number in numbers_list:
        try:
            int(number)
            numbers.append(number)
        except ValueError:
            pass
        
    return numbers


def get_winning_numbers(winning_numbers, possible_wins):
    wins = []
    for number in possible_wins:
        if number in winning_numbers:
            wins.append(number)

    return wins


def calculate_points(wins):
    if len(wins) > 0:
        return math.pow(2, len(wins) - 1)
    else:
        return 0



with open("inputs/day4.txt", "r") as f:
    data = f.read()
    cards = data.split("\n")


    points = 0

    for card in cards:
        raw_winning_numbers = card.split("|")[0]
        raw_winning_numbers = raw_winning_numbers.split(":")[1]
        raw_winning_numbers = raw_winning_numbers.split(" ")

        raw_possible_wins = card.split("|")[1]
        raw_possible_wins = raw_possible_wins.split(" ")

        winning_numbers = get_numbers_from_list(raw_winning_numbers)
        possible_wins = get_numbers_from_list(raw_possible_wins)

        print(winning_numbers)
        print(possible_wins)

        wins = get_winning_numbers(winning_numbers, possible_wins)


        points += calculate_points(wins)

print("Points won", points)