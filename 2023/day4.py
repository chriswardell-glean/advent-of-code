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
        return int(math.pow(2, len(wins) - 1))
    else:
        return 0



with open("inputs/day4.txt", "r") as f:
    data = f.read()
    cards = data.split("\n")


    points = 0

    multiplier = [1 for x in range(0, len(cards))]

    for index, card in enumerate(cards):
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
        points_from_card = calculate_points(wins)
        if points_from_card > 0:
            print(points_from_card)
            for i in range(1, points_from_card + 1):
                multiplier[i] += multiplier[index]


        points += points_from_card * multiplier[i]

print("Points won", points)

number_cards = 0
for copies in multiplier:
    number_cards += copies

print("Number cards", number_cards)