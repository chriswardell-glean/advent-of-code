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


for game_index, hands in enumerate(games):
    game_possible = True
    for hand in hands:
        if not is_hand_possible(bag_contents, hand):
            game_possible = False

    if game_possible:
        possible_games.append(game_index+1)
    else:
        impossible_games.append(game_index+1)

print(possible_games)
print(impossible_games)

total = 0
for num in possible_games:
    total+= num

print(total)