#!/usr/bin/env python3

import sys
from pokemon.game import Game

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('Not enough arguments')
    team_1, team_2 = sys.argv[1:]
    new_game = Game.create_game(team_1, team_2)
    new_game.run()
