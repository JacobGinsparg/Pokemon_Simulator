import json
from pokemon_type import Type

UNIQUE_MOVES = {
    "acupressure": None,
    "after-you": None,
    "ally-switch": None,
    "aqua-ring": None,
    "aromatherapy": None,
    "assist": None,
    "baton-pass": None,
    "belly-drum": None,
    "bestow": None,
    "block": None,
    "camouflage": None,
    "celebrate": None,
    "conversion": None,
    "conversion-2": None,
    "copycat": None,
    "curse": None,
    "defog": None,
    "destiny-bond": None,
    "detect": None,
    "disable": None,
    "doom-desire": None,
    "electrify": None,
    "encore": None,
    "endure": None,
    "entrainment": None,
    "flower-shield": None,
    "focus-energy": None,
    "follow-me": None,
    "forests-curse": None,
    "future-sight": None,
    "gastro-acid": None,
    "grudge": None,
    "guard-split": None,
    "guard-swap": None,
    "happy-hour": None,
    "heal-bell": None,
    "healing-wish": None,
    "heart-swap": None,
    "helping-hand": None,
    "hold-hands": None,
    "imprison": None,
    "kings-shield": None,
    "lock-on": None,
    "lunar-dance": None,
    "magic-coat": None,
    "magnet-rise": None,
    "mean-look": None,
    "memento": None,
    "metronome": None,
    "mimic": None,
    "mind-reader": None,
    "mirror-move": None,
    "nature-power": None,
    "pain-split": None,
    "powder": None,
    "power-split": None,
    "power-swap": None,
    "power-trick": None,
    "protect": None,
    "psych-up": None,
    "psycho-shift": None,
    "quash": None,
    "rage-powder": None,
    "recycle": None,
    "reflect-type": None,
    "refresh": None,
    "rest": None,
    "role-play": None,
    "shell-smash": None,
    "simple-beam": None,
    "sketch": None,
    "skill-swap": None,
    "sleep-talk": None,
    "snatch": None,
    "soak": None,
    "spider-web": None,
    "spiky-shield": None,
    "spite": None,
    "splash": None,
    "stockpile": None,
    "substitute": None,
    "switcheroo": None,
    "taunt": None,
    "teleport": None,
    "topsy-turvy": None,
    "transform": None,
    "trick": None,
    "trick-or-treat": None,
    "wish": None,
    "worry-seed": None
}

def _create_effect(move_data):
    category = move_data['meta']['category']['name']
    if category is 'net-good-stats':
        return _create_net_good_stats(move_data)
    elif category is 'damage':
        return _create_damage(move_data)
    elif category is 'damage+lower':
        return _create_damage_lower(move_data)
    elif category is 'damage+ailment':
        return _create_damage_ailment(move_data)
    elif category is 'ailment':
        return _create_ailment(move_data)
    elif category is 'unique':
        pass
    elif category is 'whole-field-effect':
        return _create_whole_field(move_data)
    elif category is 'damage+heal':
        return _create_damage_heal(move_data)
    elif category is 'heal':
        return _create_heal(move_data)
    elif category is 'field-effect':
        return _create_field_effect(move_data)
    elif category is 'ohko':
        return _create_ohko(move_data)
    elif category is 'force-switch':
        return _create_force_switch(move_data)
    elif category is 'swagger':
        return _create_swagger(move_data)
    else:
        #error here
        pass

def _create_net_good_stats(move_data):
    pass

def _create_damage(move_data):
    pass

def _create_damage_lower(move_data):
    pass

def _create_damage_ailment(move_data):
    pass

def _create_ailment(move_data):
    pass

def _create_whole_field(move_data):
    pass

def _create_damage_heal(move_data):
    pass

def _create_heal(move_data):
    pass

def _create_field_effect(move_data):
    pass

def _create_ohko(move_data):
    pass

def _create_force_switch(move_data):
    pass

def _create_swagger(move_data):
    pass


def _get_move_data(name):
    with open('data/moves.json') as file_data:
        all_json = json.load(file_data)
    formatted_name = name.lower().replace(' ','-')
    return all_json[formatted_name]

class MoveSet:
    def __init__(self, move_list):
        self.move1 = Move(move_list[0])
        self.move2 = Move(move_list[1])
        self.move3 = Move(move_list[2])
        self.move4 = Move(move_list[3])
        self.struggle = Move('struggle')

class Move:
    def __init__(self, name):
        move_data = _get_move_data(name)
        self.name = name
        self.type = Type[move_data['type']]
        self.effect = _create_effect(move_data)
