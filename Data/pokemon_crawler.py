#!/usr/bin/env python3

# Imports

import sys
from urllib import request
import json

# GLOBALS AND CONSTANTS

LAST_POKEMON_NUM = 721
BASE_URL = 'http://pokeapi.co/api/v2/'

# FUNCTIONS

def request_next_pokemon(poke_id):
    req = request.Request(BASE_URL + 'pokemon/' + str(poke_id), headers={'User-Agent':'Magic Browser'})
    con = request.urlopen(req)
    next_pokemon_raw = con.read()
    return json.loads(next_pokemon_raw.decode())

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

# CONTROL FLOW

if __name__ == '__main__':
    sys.stdout = open('pokemon.json', 'w')
    scrape_pokemon()
