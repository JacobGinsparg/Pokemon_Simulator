import json
import random
import math
from pokemon.data import CRIT_RATES
from pokemon.game import Game
from pokemon.type import Type
from pokemon.webster import Webster

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

def _calculate_damage(move, attacker, defender, field_crit):
    # Levels are assumed to be 100 and thus omitted
    attack = attacker.stats['attack'] if move.damage_class is 'physical' else attacker.stats['special-attack']
    defense = defender.stats['defense'] if move.damage_class is 'physical' else defender.stats['special-defense']
    stab = 1.5 if move.type in attacker.type else 1
    type_adv = move.type.advantage(defender.type)
    crit_level = min(3, field_crit + move.meta['crit_rate'])
    crit_rate = CRIT_RATES[crit_level]
    crit = 1.5 if random.randrange(0,100,1)/100 < crit_rate else 1
    other = 1 # items, abilities, field effects
    rand = random.randrange(85,100,1)/100
    mod = stab * type_adv * crit * other * rand
    return math.floor((210/250 * attack/defense * move.power + 2) * mod)

def _ailment(game, target, move):
    ailment = move.meta['ailment']['name']
    min_turns = move.meta['min_turns'] or -1
    max_turns = move.meta['max_turns'] or -1
    turns = random.randint(min_turns, max_turns)
    team = target.get_team_id()
    game.players[team][target.id].inflict_ailment(ailment, turns)

def _damage(game, target, move):
    team = target.get_team_id()
    attacker = game.get_opponent_active_pokemon(team)
    defender = target
    crit_level = game.players[team]['crit_level']
    damage = _calculate_damage(move, attacker, defender, crit_level)
    game.players[team][target.id].take_damage(damage)

def _damage_ailment(game, target, move):
    _damage(game, target, move)
    if random.randrange(0,100,1) < move.meta['ailment_chance']:
        _ailment(game, target, move)

def _damage_heal(game, target, move):
    team = target.get_team_id()
    attacker = game.get_opponent_active_pokemon(team)
    defender = target
    crit_level = game.players[team]['crit_level']
    damage = _calculate_damage(move, attacker, defender, crit_level)
    drain = math.floor(damage * move.meta['drain']/100)
    game.players[team][target.id].take_damage(damage)
    game.players[team][attacker.id].heal(drain)

def _damage_lower(game, target, move):
    _damage(game, target, move)
    if random.randrange(0,100,1) < move.effect_chance:
        _net_good_stats(game, target, move)

def _damage_raise(game, target, move):
    _damage(game, target, move)
    if random.randrange(0,100,1) < move.effect_chance:
        team = target.id[:len(target.id)/2]
        stat_target = game.get_opponent_active_pokemon(team)
        _net_good_stats(game, stat_target, move)

def _heal(game, target, move):
    team = target.get_team_id()
    max_hp = target.stats['hp'].max
    heal_amount = math.floor(max_hp * move.meta['healing']/100)
    game.players[team][target.id].heal(heal_amount)

def _field(game, target, move):
    pass

def _switch(game, target, move):
    pass

def _net_good_stats(game, target, move):
    team = target.id[:len(target.id)/2]
    for change in move.stat_changes:
        stat = change['stat']['name']
        levels = change['change']
        if levels > 0:
            game.players[team][target.id].stats[stat].raise_stage_by(levels)
        else:
            game.players[team][target.id].stats[stat].lower_stage_by(levels)

def _ohko(game, target, move):
    team = target.get_team_id()
    damage = target.stats['hp']()
    game.players[team][target.id].take_damage(damage)

def _swagger(game, target, move):
    pass

def _whole_field(game, target, move):
    pass

def _find_target_id(game, target, poke_id):
    team_id = poke_id[:len(poke_id)/2]
    if target in ['specific-move', 'selected-pokemon-me-first', 'ally', 'all-pokemon']:
        return None # these are uncommon
    elif target in ['users-field', 'user-and-allies']:
        return team_id
    elif target in ['user-or-ally','user']:
        return game.players[team_id]['team'][poke_id]
    elif target is 'opponents-field':
        return game.get_opponent(team_id)
    elif target in ['random-opponent', 'all-other-pokemon', 'selected-pokemon', 'all-opponents']:
        return game.get_opponent_active_pokemon(team_id)
    elif target is 'entire-field':
        return game.game_id
    else:
        raise Exception('Invalid target')

EFFECTS = {
    "ailment": _ailment,
    "damage": _damage,
    "damage+ailment": _damage_ailment,
    "damage+heal": _damage_heal,
    "damage+lower": _damage_lower,
    "damage+raise": _damage_raise,
    "field-effect": _field,
    "force-switch": _switch,
    "heal": _heal,
    "net-good-stats": _net_good_stats,
    "ohko": _ohko,
    "unique": None,
    "swagger": _swagger,
    "whole-field-effect": _whole_field
}

class MoveSet:
    def __init__(self, poke_id, move_list):
        self.move1 = Move(poke_id, move_list[0])
        self.move2 = Move(poke_id, move_list[1])
        self.move3 = Move(poke_id, move_list[2])
        self.move4 = Move(poke_id, move_list[3])
        self.struggle = Move(poke_id, 'struggle')

    def get_move_names(self):
        moves = [self.move1, self.move2, self.move3, self.move4]
        moves = [m for m in moves if m.pp > 0]
        if len(moves) is 0:
            moves.append(self.struggle)
        return [m.name for m in moves]

class Move:
    def __init__(self, poke_id, name):
        move_data = Webster.request_move(name)
        self.name = name
        self.accuracy = move_data['accuracy']
        self.damage_class = move_data['damage_class']
        self.effect_chance = move_data['effect_chance']
        self.meta = move_data['meta']
        self.power = move_data['power']
        self.max_pp = move_data['pp']
        self.pp = self.max_pp
        self.priority = move_data['priority']
        self.stat_changes = move_data['stat_changes']
        self.target = move_data['target']
        self.type = Type[move_data['type']]

    def use(self, game, poke_id):
        target_id = _find_target_id(game, self.target, poke_id)
        effect = EFFECTS[self.meta['category']['name']]
        effect(game, target_id, self)
