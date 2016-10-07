import json
from pokemon_type import Type

MOVE_CLASSES = {
    'physical': Physical,
    'special' : Special,
    'status'  : Status
}

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

def get_damage_class_from_json(name):
    with open('data/moves.json') as file_data:
        all_json = json.load(file_data)
    formatted_name = name.lower().replace(' ','-')
    if formatted_name in all_json:
        return all_json[formatted_name]['damage_class']
    else:
        return 'unique'

class MoveSet:
    def __init__(self, move_list):
        self.move1 = Move.create_move(move_list[0])
        self.move2 = Move.create_move(move_list[1])
        self.move3 = Move.create_move(move_list[2])
        self.move4 = Move.create_move(move_list[3])
        self.struggle = Move.create_move('struggle')

class Move:
    @classmethod
    def create_move(cls, name):
        move_class = get_damage_class_from_json(name)
        if move_class is 'unique':
            return UNIQUE_MOVES[name]()
        else:
            return MOVE_CLASSES[move_class](name)

class Physical(Move):
    def __init__(self, name):
        pass

class Special(Move):
    def __init__(self, name):
        pass

class Status(Move):
    def __init__(self, name):
        pass
