import json
from nature import Nature

_stage_mods = {
    -6: 2/8
    -5: 2/7
    -4: 2/6
    -3: 2/5
    -2: 2/4
    -1: 2/3
    0: 2/2
    1: 3/2
    2: 4/2
    3: 5/2
    4: 6/2
    5: 7/2
    6: 8/2
}

class StatSet:
    def __init__(self, name, nature, evs, ivs):
        with open('data/pokemon.json') as file_data:
            all_json = json.load(file_data)
        stats = all_json[name.lower()][base_stats]
        self.hp = HPStat(stats['hp'], evs['HP'], ivs['HP'])
        self.attack = Stat(stats['attack'], evs['Atk'], ivs['Atk'], nature.value[0])
        self.defense = Stat(stats['defense'], evs['Def'], ivs['Def'], nature.value[1])
        self.speed = Stat(stats['speed'], evs['Spe'], ivs['Spe'], nature.value[2])
        self.sp_attack = Stat(stats['special-attack'], evs['SpA'], ivs['SpA'], nature.value[3])
        self.sp_defense = Stat(stats['special-defense'], evs['SpD'], ivs['SpD'], nature.value[4])

class Stat:
    def __init__(self, base, ev, iv, nature_mod):
        self.base = base
        self.ev = ev
        self.iv = iv
        self.nature_mod = nature_mod
        self.stage = 0

    def __call__(self):
        # Level is assumed to be 100 and is thus omitted
        return ((2 * self.base) + self.iv + (self.ev / 4) + 5) * self.nature_mod * _stage_mods[self.stage]

    def raise_stage_by(self, num_stages):
        self.stage = min(self.stage + num_stages, 6)

    def lower_stage_by(self, num_stages):
        self.stage = max(self.stage - num_stages, -6)

class HPStat(Stat):
    def __init__(self, base, ev, iv):
        self.base = base
        self.ev = ev
        self.iv = iv

    def __call__(self):
        # Level is assumed to be 100 and is thus omitted
        return (2 * self.base) + self.iv + (self.ev / 4) + 110
