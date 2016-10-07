import json
from pokemon_type import Type

MOVE_CLASSES = {
    'physical': Physical,
    'special' : Special,
    'status'  : Status
}

UNIQUE_MOVES = {

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
