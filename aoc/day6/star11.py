def count_orbits(orbit_map_str):
    orbit_map = parse_orbit_map(orbit_map_str)

    result = 0
    for obj in orbit_map.keys():
        result += len(path_to_com(obj, orbit_map))

    return result


def parse_orbit_map(orbit_map_str):
    orbit_map_str = orbit_map_str.strip()
    orbit_map_list = [line.split(')') for line in orbit_map_str.split('\n')]

    result = {}

    # each key is an orbiting object that orbits around the object stored in its value
    for orbit in orbit_map_list:
        obj = orbit[0]
        orbiting_obj = orbit[1]
        result[orbiting_obj] = obj

    return result


def path_to_com(obj, orbit_dict):
    curr_obj = obj
    result = []

    while curr_obj != 'COM':
        curr_obj = orbit_dict[curr_obj]
        result.append(curr_obj)

    return result


def answer():
    from pathlib import Path
    curr_dir = Path(__file__).parent.absolute()

    with open(curr_dir / 'input.txt') as input:
        return count_orbits(input.read())

if __name__ == '__main__':
    print(answer())
