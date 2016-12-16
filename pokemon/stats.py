import json
import math
import pokemon.data
import pokemon.nature

class StatSet:
    def __init__(self, stats, nature, evs, ivs):
        self.hp = HPStat(stats['hp'], evs['HP'], ivs['HP'])
        self.attack = Stat(stats['attack'], evs['ATK'], ivs['ATK'], nature.attack())
        self.defense = Stat(stats['defense'], evs['DEF'], ivs['DEF'], nature.defense())
        self.speed = Stat(stats['speed'], evs['SPE'], ivs['SPE'], nature.speed())
        self.sp_attack = Stat(stats['special-attack'], evs['SPA'], ivs['SPA'], nature.sp_attack())
        self.sp_defense = Stat(stats['special-defense'], evs['SPD'], ivs['SPD'], nature.sp_defense())

    def __getitem__(self, key):
        if key is 'hp':
            return self.hp
        elif key is 'attack':
            return self.attack
        elif key is 'defense':
            return self.defense
        elif key is 'speed':
            return self.speed
        elif key is 'special-attack':
            return self.sp_attack
        elif key is 'special-defense':
            return self.sp_defense
        else:
            raise Exception('Invalid stat')

class Stat:
    def __init__(self, base, ev, iv, nature_mod):
        self.base = base
        self.ev = ev
        self.iv = iv
        self.nature_mod = nature_mod
        self.stage = 0

    def __call__(self):
        # Level is assumed to be 100 and is thus omitted
        return math.floor(((2 * self.base) + self.iv + (self.ev / 4) + 5) * self.nature_mod * pokemon.data.STAGE_MODS[self.stage])

    def raise_stage_by(self, num_stages):
        self.stage = min(self.stage + num_stages, 6)

    def lower_stage_by(self, num_stages):
        self.stage = max(self.stage - num_stages, -6)

class HPStat(Stat):
    def __init__(self, base, ev, iv):
        self.base = base
        self.ev = ev
        self.iv = iv
        # Level is assumed to be 100 and is thus omitted
        self.max = math.floor((2 * self.base) + self.iv + (self.ev / 4) + 110)
        self.current = self.max

    def __call__(self):
        return self.current

    def take_damage(self, amount):
        self.current = max(0, self.current - amount)

    def heal(self, amount):
        self.current = min(self.max, self.current + amount)
