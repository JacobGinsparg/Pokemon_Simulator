import json
import uuid
import pokemon.data
import pokemon.move
import pokemon.nature
import pokemon.stats
import pokemon.type
import pokemon.webster

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
        poke_json = pokemon.webster.Webster.request_pokemon(name)
        self.id = team_id + str(uuid.uuid4())
        self.name = name
        self.nickname = nickname
        self.nature = pokemon.nature.Nature[nature]
        self.type = [pokemon.type.Type[t] for t in poke_json['type']]
        self.item = None
        self.ability = None
        self.moveset = pokemon.move.MoveSet(self.id, move_list)
        self.stats = pokemon.stats.StatSet(poke_json['base_stats'], self.nature, evs, ivs)
        self.ailments = {
            'hard': {'name': None, 'turns': -1},
            'soft': []
        }

    def get_team_id(self):
        return self.id[:len(self.id)//2]

    def take_damage(self, amount):
        self.stats['hp'].take_damage(amount)
        if self.stats['hp']() is 0:
            self.faint()

    def heal(self, amount):
        self.stats['hp'].heal(amount)

    def inflict_ailment(self, ailment, turns):
        if ailment in pokemon.data.HARD_AILMENTS and not self.is_afflicted_by(ailment):
            self.ailments['hard'] = {
                'name': ailment,
                'turns': turns
            }
        elif ailment in pokemon.data.SOFT_AILMENTS and not self.is_afflicted_by(ailment):
            self.ailments['soft'].append({
                'name': ailment,
                'turns': turns
            })

    def is_afflicted_by(self, ailment):
        return ailment in [a['name'] for a in self.ailments['soft']] or ailment is self.ailments['hard']['name']

    def faint(self):
        self.ailments['hard'] = {
            'name': 'faint',
            'turns': -1
        }

    def get_moves(self):
        return self.moveset.get_move_names()

    def get_move(self, name):
        return self.moveset.get_move(name)
