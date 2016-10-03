#!/usr/bin/env python3

# Imports

import json
import sys
from urllib import request

# GLOBALS AND CONSTANTS

LAST_POKEMON_NUM = 721
LAST_ABILITY_NUM = 191
LAST_MOVE_NUM = 621
BASE_URL = 'http://pokeapi.co/api/v2/'
HEADERS = {'User-Agent':'Magic Browser'}

# FUNCTIONS

def request_next(url):
    req = request.Request(url, headers=HEADERS)
    con = request.urlopen(req)
    next_raw = con.read()
    return json.loads(next_raw.decode())

# Pokemon

def request_next_pokemon(poke_id):
    return request_next(BASE_URL + 'pokemon/' + str(poke_id))

def scrape_pokemon():
    pokemon = {}
    for i in range(1, LAST_POKEMON_NUM + 1):
        poke_json = request_next_pokemon(i)
        pokemon[poke_json['name']] = {
            'type': [t['type']['name'] for t in poke_json['types']],
            'base_stats': {s['stat']['name']: s['base_stat'] for s in poke_json['stats'] }
        }
    output_json = json.dumps(pokemon, sort_keys=True, indent=4)
    print(output_json)

# Moves

def request_next_move(move_id):
    return request_next(BASE_URL + 'move/' + str(move_id))

def scrape_moves():
    moves = {}
    for i in range(1, LAST_MOVE_NUM + 1):
        move_json = request_next_move(i)
        moves[move_json['name']] = {
            'accuracy': move_json['accuracy'],
            'effect_chance': move_json['effect_chance'],
            'pp': move_json['pp'],
            'priority': move_json['priority'],
            'power': move_json['power'],
            'damage_class': move_json['damage_class']['name'],
            'meta': move_json['meta'],
            'stat_changes': move_json['stat_changes'],
            'type': move_json['type']['name']
        }
    output_json = json.dumps(moves, sort_keys=True, indent=4)
    print(output_json)

# CONTROL FLOW

if __name__ == '__main__':
    sys.stdout = open('pokemon.json', 'w')
    scrape_pokemon()
    sys.stdout = open('moves.json', 'w')
    scrape_moves()
