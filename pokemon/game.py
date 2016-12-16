import uuid

def _team_from_file_path(player_id, path):
    team = Parser.parse_team(player_id, path)
    return {
        'team': team,
        'active_id': list(team)[0],
        'crit_level': 0,
        'entry_hazards': [],
        'player_field_effects': []
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
        game.player_actions = []
        game.bot_queue = []
        game.eot_queue = []
        return game

    def run(self):
        while(self.combatants_available()):
            self.prompt_player_actions()
            self.perform_bot_actions()
            self.perform_pre_combat_actions()
            self.perform_player_actions()
            self.perform_post_combat_actions()
            self.perform_eot_actions()
        self.announce_winner()

    def combatants_available(self):
        both_teams_good = True
        for team in [self.players[p_id]['team'] for p_id in self.players]:
            team_has_available_pokemon = False
            for poke in [team[poke_id] for poke_id in team]:
                if not poke.is_afflicted_by('faint'):
                    team_has_available_pokemon = True
                    break
            if not team_has_available_pokemon:
                both_teams_good = False
                break
        return both_teams_good

    def prompt_player_actions(self):
        for player in self.players:
            player_choice = None
            while player_choice is None:
                _print_player_choices(self.players[player])
                choice = input('Your choice: ')
                player_choice = _get_choice_for_player(self.players[player], choice)
            player_actions.append(player_choice)

    def _print_player_choices(player):
        available = self.get_player_available_pokemon(player)
        active = self.get_player_active_pokemon(player)
        non_active = [poke for poke in available if poke.id is not active.id]
        moves = active.get_moves()
        print('Choose from the following available actions.\nUse a move:')
        for move in moves:
            print(move)
        if len(non_active) > 0:
            print('Switch to a different Pokémon:')
            for poke in non_active:
                print(poke.name)

    def _get_choice(player, choice_string):
        available = self.get_player_available_pokemon(player)
        active = self.get_player_active_pokemon(player)
        non_active = [poke for poke in available if poke.id is not active.id]
        moves = active.get_moves()
        if choice_string in non_active: # Using a move
            return ('move', active.id, choice_string)
        elif choice_string in moves: # Switching out
            return ('switch', active.id, choice_string)
        else: # Not a valid move or pokemon
            return None

    def perform_bot_actions(self):
        pass

    def perform_pre_combat_actions(self):
        pass

    def perform_player_actions(self):
        for action in self.player_actions:
            active_id = action[1]
            team_id = active_id[:len(active_id)/2]
            active = self.get_player_active_pokemon(team_id)
            if action[0] is 'move':
                move = active.get_move(action[2])
                move.use(self, active_id)
            elif action[0] is 'switch':
                available = self.get_player_available_pokemon(team_id)
                name = action[2]
                self.players[team_id]['active_id'] = [p_id for p_id in available if available[p_id].name is name][0]
            else:
                raise Exception('Invalid player action')

    def perform_post_combat_actions(self):
        pass

    def perform_eot_actions(self):
        pass

    def announce_winner(self):
        pass

    def get_opponent(self, team_id):
        return [i for i in list(self.players.keys()) if i is not team_id][0]

    def get_opponent_active_pokemon(self, team_id):
        opponent_id = self.get_opponent(team_id)
        active_id = self.players[opponent_id]['active_id']
        return self.players[opponent_id]['team'][active_id]

    def get_player_active_pokemon(self, team_id):
        active_id = self.players[team_id]['active_id']
        return self.players[team_id]['team'][active_id]

    def get_player_available_pokemon(self, team_id):
        team = self.players['team_id']['team']
        return [team[poke] for poke in team]
