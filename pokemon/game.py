import uuid

def _team_from_file_path(player_id, path):
    team = Parser.parse_team(path)
    return {
        "team": team,
        "active_id": team[0],
        "crit_level": 0,
        "entry_hazards": []
    }

class Game:
    @classmethod
    def createGame(cls, team_path_1, team_path_2):
        game = cls()
        # Game state
        id_1 = str(uuid.uuid4())
        id_2 = str(uuid.uuid4())
        game.players = {
            id_1: _team_from_file_path(id_1, team_path_1),
            id_2: _team_from_file_path(id_2, team_path_2)
        }
        game.weather = None
        game.weather_turns = 0
        game.trick_room = False
        game.trick_room_turns = 0
        # Actions queues
        game.bot_queue = []
        game.eot_queue = []
        return game

    def run():
        while(self.combatants_available()):
            self.prompt_player_actions()
            self.perform_pre_turn_actions()
            self.perform_player_actions()
            self.perform_eot_actions()
        self.announce_winner()

    def combatants_available():
        pass

    def prompt_player_actions():
        pass

    def perform_pre_turn_actions():
        pass

    def perform_player_actions():
        pass

    def perform_eot_actions():
        pass

    def announce_winner():
        pass
