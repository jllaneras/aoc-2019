#!/usr/bin/env python3

import star5


def test_find_closest_wire_cross_distance(wire_paths, expected_distance):
    actual_distance = star5.find_closest_wire_cross_distance(wire_paths)
    assert actual_distance == expected_distance, f'For the following wire paths, the expected distance was {expected_distance} but the distance found was {actual_distance}:\n{wire_paths}'


if __name__ == '__main__':
    TEST_INPUTS = [
        (
            'R8,U5,L5,D3\nU7,R6,D4,L4',
            6
        ),
        (
            'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83',
            159
        ),
        (
            'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7',
            135
        )
    ]

    for i, test_input in enumerate(TEST_INPUTS):
        print(f'====Test {i}====')
        test_find_closest_wire_cross_distance(test_input[0], test_input[1])
        print('Test passed')
