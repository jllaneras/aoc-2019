#!/usr/bin/env python3

from star11 import parse_orbit_map, path_to_com


def min_orbit_transfers_between_you_and_santa(orbit_map_str):
    orbit_map = parse_orbit_map(orbit_map_str)

    # If Santa is on your path to the Center of Mass (COM) then it's easy:
    # just count the number of orbital transfers between you and Santa
    your_path_to_com = path_to_com('YOU', orbit_map)
    if 'SAN' in your_path_to_com:
        return your_path_to_com.index('SAN')

    # If santa is not on your path to the Center of Mass (COM) then
    # we need to find the closest common object, that is the closest object
    # that is both in your path to COM and in Santa's path to COM. The
    # minimum orbital transfers between you and Santa is the number of
    # orbital transfers between you and the common object plus the ones
    # between Santa and that same common object.
    santas_path_to_com = path_to_com('SAN', orbit_map)
    common_obj = find_closest_common_object(your_path_to_com, santas_path_to_com)
    return your_path_to_com.index(common_obj) + santas_path_to_com.index(common_obj)


def find_closest_common_object(your_path_to_com, santas_path_to_com):
    your_path_set = set(your_path_to_com)
    for obj in santas_path_to_com:
        if obj in your_path_set:
            # worst case the closest common object will be COM
            return obj


if __name__ == '__main__':
    with open('input.txt') as input:
        print(min_orbit_transfers_between_you_and_santa(input.read()))
