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

    # nightmare
    # trap
    # infatuation
    # confusion
    # poison
    # burn
    # freeze
    # sleep
    # paralysis

def create_physical_move(move_json):
    return {}

def create_special_move(move_json):
    return {}

def create_status_move(move_json):
    return {}

def request_next_move(move_id):
    return request_next(BASE_URL + 'move/' + str(move_id))

def scrape_moves():
    moves = {}
    for i in range(1, LAST_MOVE_NUM + 1):
        move_json = request_next_move(i)
        damage_class = move_json['damage_class']['name']
        if damage_class is 'physical':
            moves[move_json['name']] = create_physical_move(move_json)
        elif damage_class is 'special':
            moves[move_json['name']] = create_special_move(move_json)
        elif damage_class is 'status':
            moves[move_json['name']] = create_status_move(move_json)
        else:
            raise RuntimeError('Not a physical, special, or status move')
        # moves[move_json['name']] = {
        #     'accuracy': move_json['accuracy'],
        #     'effect_chance': move_json['effect_chance'],
        #     'effect': determine_effect(ailments, move_json['name']),
        #     'power': move_json['power'],
        #     'pp': move_json['pp'],
        #     'priority': move_json['priority'],
        #     'damage_class': move_json['damage_class']['name'],
        #     'type': move_json['type']['name'],
        # }
    output_json = json.dumps(moves, sort_keys=True, indent=4)
    print(output_json)

# CONTROL FLOW

if __name__ == '__main__':
    sys.stdout = open('pokemon.json', 'w')
    scrape_pokemon()
    sys.stdout = open('moves.json', 'w')
    scrape_moves()
