#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    actions, possible_combinations = ['rock', 'paper', 'scissors'], []

    def get_possible_combination(rounds_left, result):
        if rounds_left < 1:
            possible_combinations.append(result)
            return

        for action in actions:
            get_possible_combination(rounds_left - 1, [*result, action])

    get_possible_combination(n, [])
    return possible_combinations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
