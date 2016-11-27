
class Game:
    @classmethod
    def createGame(cls, team_path_1, team_path_2):
        game = cls()
        # Game state
        game.player1 = Parser.parse_team(team_path_1)
        game.player2 = Parser.parse_team(team_path_2)
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
