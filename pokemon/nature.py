from enum import Enum

class Nature(Enum):
    Hardy   = [0,0,0,0,0]
    Lonely  = [1,-1,0,0,0]
    Brave   = [1,0,-1,0,0]
    Adamant = [1,0,0,-1,0]
    Naughty = [1,0,0,0,-1]
    Bold    = [-1,1,0,0,0]
    Docile  = [0,0,0,0,0]
    Relaxed = [0,1,-1,0,0]
    Impish  = [0,1,0,-1,0]
    Lax     = [0,1,0,0,-1]
    Timid   = [-1,0,1,0,0]
    Hasty   = [0,-1,1,0,0]
    Serious = [0,0,0,0,0]
    Jolly   = [0,0,1,-1,0]
    Naive   = [0,0,1,0,-1]
    Modest  = [-1,0,0,1,0]
    Mild    = [0,-1,0,1,0]
    Quiet   = [0,0,-1,1,0]
    Bashful = [0,0,0,0,0]
    Rash    = [0,0,0,1,-1]
    Calm    = [-1,0,0,0,1]
    Gentle  = [0,-1,0,0,1]
    Sassy   = [0,0,-1,0,1]
    Careful = [0,0,0,-1,1]
    Quirky  = [0,0,0,0,0]

    def attack(self):
        return 1 + 0.1 * self.value[0]

    def defense(self):
        return 1 + 0.1 * self.value[1]

    def speed(self):
        return 1 + 0.1 * self.value[2]

    def sp_attack(self):
        return 1 + 0.1 * self.value[3]

    def sp_defense(self):
        return 1 + 0.1 * self.value[4]
