import json
import uuid

from move import MoveSet
from nature import Nature
from pokemon_type import Type
from stats import StatSet

def _normalize_value_dict(v_dict, base):
    normalized_values = {}
    for stat in ['HP', 'ATK', 'DEF', 'SPE', 'SPA', 'SPD']:
        if stat not in v_dict:
            normalized_values[stat] = base
        else:
            normalized_values[stat] = v_dict[stat]
    return normalized_values

def _normalize_evs(ev_dict):
    return _normalize_value_dict(ev_dict, 0)

def _normalize_ivs(iv_dict):
    return _normalize_value_dict(iv_dict, 31)

class Pokemon:
    def __init__(self, team_id, name, nickname, nature, item, ability, move_list, ev_dict, iv_dict):
        evs = _normalize_evs(ev_dict)
        ivs = _normalize_ivs(iv_dict)
        poke_json = Webster.request_pokemon(name)
        self.id = team_id + str(uuid.uuid4())
        self.name = name
        self.nickname = nickname
        self.nature = Nature[nature]
        self.type = [Type[t] for t in poke_json['type']]
        self.item = None
        self.ability = None
        self.moveset = MoveSet(self.id, move_list)
        self.stats = StatSet(poke_json['base_stats'], self.nature, evs, ivs)

    def get_team_id(self):
        return self.id[:len(self.id)/2]
