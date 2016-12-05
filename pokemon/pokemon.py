import json
import uuid

from move import MoveSet
from nature import Nature
from pokemon_type import Type
from stats import StatSet

HARD_AILMENTS = [
    'poison',
    'burn',
    'freeze',
    'sleep',
    'paralysis'
]

SOFT_AILMENTS = [
    'nightmare',
    'trap',
    'infatuation',
    'confusion',
    'torment',
    'disable',
    'yawn',
    'heal-block',
    'no-type-immunity',
    'leech-seed',
    'embargo',
    'perish-song',
    'ingrain'
]

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
        self.ailments = {
            'hard': None
            'soft': []
        }

    def get_team_id(self):
        return self.id[:len(self.id)/2]

    def take_damage(self, amount):
        self.stats['hp'].take_damage(amount)

    def heal(self, amount):
        self.stats['hp'].heal(amount)

    def inflict_ailment(self, ailment, turns):
        if ailment in HARD_AILMENTS and not self.is_afflicted_by(ailment):
            self.ailments['hard']['name'] = ailment
            self.ailments['hard']['turns'] = turns
        elif ailment in SOFT_AILMENTS and not self.is_afflicted_by(ailment):
            self.ailments['soft'].append({
                'name': ailment,
                'turns': turns
            })

    def is_afflicted_by(self, ailment):
        return ailment in [a['name'] for a in self.ailments['soft']] + [self.ailments['hard']['name']]
