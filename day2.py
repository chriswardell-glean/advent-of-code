from typing import List

def parse_input(raw_games: List[str]) -> List[dict]:
    games = []
    for raw_game in raw_games:
        hands = []
        raw_game = raw_game.split(":")[1]
        raw_hands = raw_game.split(";")

        for raw_hand in raw_hands:
            hand = {}
            raw_colours = raw_hand.split(",")
            for raw_colour in raw_colours:
                number_colour_list = raw_colour.strip().split(" ")
                number = int(number_colour_list[0])
                colour = number_colour_list[1]
                hand[colour] = number
            
            hands.append(hand)

        games.append(hands)
    return games


def is_hand_possible(bag_contents, hand) -> bool:
    for colour, number in hand.items():
        # if colour in hand is not in bag
        if colour not in bag_contents:
            return False
        
        # if more of one colour shown in a hand than is in bag
        if number > bag_contents[colour]:
            return False
        
        # print(colour, number)

    return True


def get_power_of_game(bag_contents, hands) -> int:
    minimums = {}

    for hand in hands:
        for colour, number in hand.items():
            # no current minimum set, this is the new minimum
            if colour not in minimums:
                minimums[colour] = number
            # number is higher than minimum - new minimum required
            elif minimums[colour] < number:
                minimums[colour] = number


    power = 1
    for _, minimum in minimums.items():
        power *= minimum
    
    return power


with open("./inputs/day2.txt", "r") as f:
    input = f.read()


games = parse_input(input.split("\n"))
print(games)

bag_contents = {
    "red": 12,
    "blue": 14,
    "green": 13
}


possible_games = []
impossible_games = []
power_game_minimums = []

for game_index, hands in enumerate(games):
    game_possible = True
    for hand in hands:
        if not is_hand_possible(bag_contents, hand):
            game_possible = False

    if game_possible:
        possible_games.append(game_index+1)
    else:
        impossible_games.append(game_index+1)

    power_game_minimums.append(get_power_of_game(bag_contents, hands))

print(possible_games)
print(impossible_games)

total = 0
for num in possible_games:
    total+= num

print("Total sum of possible games", total)



total_power = 0
for num in power_game_minimums:
    total_power+= num

print("Total sum of powers", total_power)