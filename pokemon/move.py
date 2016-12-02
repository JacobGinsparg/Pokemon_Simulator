import json
from game import Game
from pokemon_type import Type
from webster import Webster

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

EFFECTS = {
    "net-good-stats": None
    "damage": None
    "damage+lower": None
    "damage+ailment": None
    "ailment": None
    "unique": None
    "whole-field-effect": None
    "damage+heal": None
    "damage+raise": None
    "heal": None
    "field-effect": None
    "ohko": None
    "force-switch": None
    "swagger": None
}

def _find_target_id(game, target, poke_id):
    team_id = poke_id[:len(poke_id)/2]
    if target in ['specific-move', 'selected-pokemon-me-first', 'ally']:
        return None # these are uncommon
    elif target in ['users-field', 'user-and-allies']:
        return team_id
    elif target in ['user-or-ally','user']:
        return poke_id
    elif target is 'opponents-field':
        return game.get_opponent(team_id)
    elif target in ['random-opponent', 'all-other-pokemon', 'selected-pokemon', 'all-opponents']:
        return game.get_opponent_active_pokemon(team_id)
    elif target is 'entire-field':
        return game.game_id
    elif target is 'all-pokemon':
        return [poke_id, game.get_opponent_active_pokemon(team_id)]
    else:
        raise Exception('Invalid target')

class MoveSet:
    def __init__(self, poke_id, move_list):
        self.move1 = Move(poke_id, move_list[0])
        self.move2 = Move(poke_id, move_list[1])
        self.move3 = Move(poke_id, move_list[2])
        self.move4 = Move(poke_id, move_list[3])
        self.struggle = Move(poke_id, 'struggle')

class Move:
    def __init__(self, poke_id, name):
        move_data = Webster.request_move(name)
        self.name = name
        self.accuracy = move_data['accuracy']
        self.damage_class = move_data['damage_class']
        self.effect_chance = move_data['effect_chance']
        self.meta = move_data['meta']
        self.power = move_data['power']
        self.pp = move_data['pp']
        self.priority = move_data['priority']
        self.stat_changes = move_data['stat_changes']
        self.target = move_data['target']
        self.type = Type[move_data['type']]

    def use(self, game, poke_id):
        target_id = _find_target_id(game, self.target, poke_id)
        effect = EFFECTS[self.meta['category']['name']]
        effect(game, target_id)
