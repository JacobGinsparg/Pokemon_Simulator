from enum import Enum
from pokemon.data import TYPE_CHART

class Type(Enum):
    normal  =  0
    fighting = 1
    flying  =  2
    poison  =  3
    ground  =  4
    rock    =  5
    bug     =  6
    ghost   =  7
    steel   =  8
    fire    =  9
    water   =  10
    grass   =  11
    electric = 12
    psychic =  13
    ice     =  14
    dragon  =  15
    dark    =  16
    fairy   =  17

    def __str__(self):
        return self.name.title()

    def advantage(self, types):
        total_advantage = 1
        for t in set(types):
            total_advantage *= TYPE_CHART[self.value][Type[t].value]
        return total_advantage
