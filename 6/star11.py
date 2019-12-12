#!/usr/bin/env python3


def count_orbits(orbit_map):
    orbit_map = orbit_map.strip()
    orbit_map = [line.split(')') for line in orbit_map.split('\n')]
    
    orbit_dict = {}

    # each key is an orbiting object that orbits around the object stored in its value
    for orbit in orbit_map:
        obj = orbit[0]
        orbiting_obj = orbit[1]
        orbit_dict[orbiting_obj] = obj

    result = 0
    for obj in orbit_dict.keys():
        result += _count_orbits_object(obj, orbit_dict)

    return result


def _count_orbits_object(obj, orbit_dict):
    curr_obj = obj
    result = 0

    while curr_obj != 'COM':
        curr_obj = orbit_dict[curr_obj]
        result += 1

    return result


if __name__ == '__main__':
    with open('input.txt') as input:
        print(count_orbits(input.read()))
