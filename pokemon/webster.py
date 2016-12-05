import json
import sys
from urllib import request

BASE_URL = 'http://pokeapi.co/api/v2/'
HEADERS = {'User-Agent':'Magic Browser'}

def _request_resource(url):
    req = request.Request(url, headers=HEADERS)
    con = request.urlopen(req)
    raw = con.read()
    return json.loads(raw.decode())

class Webster:
    @classmethod
    def request_pokemon(cls, name):
        formatted_name = name.lower().replace(' ','-')
        poke_json = _request_resource(BASE_URL + 'pokemon/' + formatted_name)
        poke_dict = {
            'weight': poke_json['weight'],
            'abilities': [a['ability']['name'] for a in poke_json['abilities']],
            'moves': [m['move']['name'] for m in poke_json['moves']],
            'base_stats': {s['stat']['name']: s['base_stat'] for s in poke_json['stats']},
            'type': [t['type']['name'] for t in poke_json['types']]
        }
        return poke_dict

    @classmethod
    def request_move(cls, name):
        formatted_name = name.lower().replace(' ','-')
        move_json = _request_resource(BASE_URL + 'move/' + formatted_name)
        move_dict = {
            'accuracy': move_json['accuracy'],
            'effect_chance': move_json['effect_chance'],
            'pp': move_json['pp'],
            'priority': move_json['priority'],
            'power': move_json['power'],
            'damage_class': move_json['damage_class']['name'],
            'meta': move_json['meta'],
            'stat_changes': move_json['stat_changes'],
            'target': move_json['target']['name'],
            'type': move_json['type']['name']
        }
        return move_dict
