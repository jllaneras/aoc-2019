#!/usr/bin/env python3

import star6


def test_find_fewest_combined_steps_to_intersection(wire_paths, expected_steps):
    steps = star6.find_fewest_combined_steps_to_intersection(wire_paths)
    assert steps == expected_steps, f'For the following wire paths, the expected combined steps were {expected_steps} but the amount of steps found was {steps}:\n{wire_paths}'


if __name__ == '__main__':
    TEST_INPUTS = [
        (
            'R8,U5,L5,D3\nU7,R6,D4,L4',
            30
        ),
        (
            'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83',
            610
        ),
        (
            'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7',
            410
        )
    ]

    for i, test_input in enumerate(TEST_INPUTS):
        print(f'====Test {i}====')
        test_find_fewest_combined_steps_to_intersection(test_input[0], test_input[1])
        print('Test passed')
