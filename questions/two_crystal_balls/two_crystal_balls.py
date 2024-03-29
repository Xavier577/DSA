import math

"""
Give two crystal balls that will break if dropped from a high enough distance,
determine the exact spot in which it will break in the most optimized way.

Example

input

floor_lvl = [False, False, False, False, False, True, True, True, True, True]

output

5
"""


def two_crystal_balls(floor_lvls: list[bool]) -> int:
    floor_lvl_len = len(floor_lvls)

    jump_amount = math.floor(math.sqrt(floor_lvl_len))

    i = jump_amount

    break_point = -1

    while i < floor_lvl_len:
        if floor_lvls[i] == True:
            break

        i += jump_amount

    i -= jump_amount

    j = 0

    while j < jump_amount and i < floor_lvl_len:
        if floor_lvls[i] == True:
            break_point = i
            break

        j += 1
        i += 1

    return break_point
