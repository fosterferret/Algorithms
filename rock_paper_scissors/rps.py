#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    actions = ['rock', 'paper', 'scissors']
    possible_plays = []

    def get_possible_play(rounds_left, result):
        if rounds_left < 1:
            possible_plays.append(result)
            return

        for action in actions:
            get_possible_play(rounds_left - 1, [*result, action])

    get_possible_play(n, [])
    return possible_plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
