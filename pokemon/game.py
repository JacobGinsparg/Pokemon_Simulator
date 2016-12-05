import uuid

def _team_from_file_path(player_id, path):
    team = Parser.parse_team(player_id, path)
    return {
        "team": team,
        "active_id": list(team)[0],
        "crit_level": 0,
        "entry_hazards": [],
        "player_field_effects": []
    }

class Game:
    @classmethod
    def createGame(cls, team_path_1, team_path_2):
        game = cls()
        # Game state
        game.game_id = str(uuid.uuid4())
        id_1 = str(uuid.uuid4())
        id_2 = str(uuid.uuid4())
        game.players = {
            id_1: _team_from_file_path(id_1, team_path_1),
            id_2: _team_from_file_path(id_2, team_path_2)
        }
        game.field_effects = []
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
            self.perform_bot_actions()
            self.perform_pre_combat_actions()
            self.perform_player_actions()
            self.perform_post_combat_actions()
            self.perform_eot_actions()
        self.announce_winner()

    def combatants_available():
        pass

    def prompt_player_actions():
        pass

    def perform_bot_actions():
        pass

    def perform_pre_combat_actions():
        pass

    def perform_player_actions():
        pass

    def perform_post_combat_actions():
        pass

    def perform_eot_actions():
        pass

    def announce_winner():
        pass

    def get_opponent(self, team_id):
        return [i for i in list(self.players.keys()) if i is not team_id][0]

    def get_opponent_active_pokemon(self, team_id):
        opponent_id = self.get_opponent(team_id)
        return self.players[opponent_id][active_id]
