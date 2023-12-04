not_symbols = [str(x) for x in range(0,10)] + ["."]

def get_all_symbol_coords(data):
    symbol_coords = []

    for y, row in enumerate(data):
        for x, digit in enumerate(row):
            # not symbol - must be symbol
            if digit not in not_symbols:
                symbol_coords.append((x, y))

    return symbol_coords


def get_part_and_coords_at_coord(data, x, y):
    # part numbers after targeted coord to end of line
    part_coords = []
    lhs_part_number = ""
    center_part_number = data[y][x]
    rhs_part_number = ""

    numbers = [str(x) for x in range(0, 10)]

    for i in range(x-1, -1, -1):
        # if no longer a number, must be end of part number
        if data[y][i] not in numbers:
            break

        lhs_part_number = data[y][i] + lhs_part_number
        part_coords.append((i, y))

    part_coords.append((x, y))

    for i in range(x+1, len(data[y])-1):
        # if no longer a number, must be end of part number
        if data[y][i] not in numbers:
            break

        rhs_part_number += data[y][i]
        part_coords.append((i, y))

    return (lhs_part_number+center_part_number+rhs_part_number, part_coords)
    




def get_parts_adjacent_to_coord(data, symbol_coord):
    print("****** Symbol coord", symbol_coord)
    max_y = len(data) - 1
    max_x = len(data[0]) - 1

    adjacent_offset_coords = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            adjacent_offset_coords.append((x, y))

    # adjacent coords within data frame
    adjacent_coords = []
    for offset_coord in adjacent_offset_coords:
        adjacent_coord = (symbol_coord[0] + offset_coord[0], symbol_coord[1] + offset_coord[1])
        if adjacent_coord[0] < 0 or adjacent_coord[0] > max_x or adjacent_coord[1] < 0 or adjacent_coord[1] > max_y:
            continue
        else:
            adjacent_coords.append(adjacent_coord)

    print("Adjacent coords", adjacent_coords)

    found_part_details = []

    # part numbers
    for adjacent_coord in adjacent_coords:
        x = adjacent_coord[0]
        y = adjacent_coord[1]
        # y then x - go down rows then along the rows
        try:
            int(data[y][x])
            part_number, part_coords = get_part_and_coords_at_coord(data, x, y)
            found_part_details.append({
                "number": part_number,
                "coords": part_coords
            })
        # not an int so skip coord
        except ValueError:
            continue

    return found_part_details


def deduplicate_parts_details(parts_details):
    part_numbers = []
    part_coords = []

    for detail in parts_details:
        number = detail["number"]
        coords = detail["coords"]


        # not a dupe if part number not in list and its coords also are not
        if number not in part_numbers and coords[0] not in part_coords:
            part_numbers.append(number)
            for coord in part_coords:
                part_coords.append(coord)

    return part_numbers


with open("inputs/day3-example.txt") as f:
    data = f.read().split("\n")
    for i, row in enumerate(data):
        data[i] = [*row]

    for row in data:
        print(row)

    symbol_coords = get_all_symbol_coords(data)
    print("Symbol coords", symbol_coords)


    adjacent_parts_details = []
    for coord in symbol_coords:
        adjacent_parts_details += get_parts_adjacent_to_coord(data, coord)

    print(adjacent_parts_details)


    deduplicated_part_numbers = deduplicate_parts_details(adjacent_parts_details)


    total = 0
    for number in deduplicated_part_numbers:
        total += int(number)

    print("Total", total)