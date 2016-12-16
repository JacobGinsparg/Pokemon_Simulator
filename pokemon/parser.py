import re
import pokemon.pokemon

NAME_LINE = re.compile(r"^(?P<name>[^@\(\)]+)( @ (?P<item>.+))?$")
NICKNAME_LINE = re.compile(r"^(?P<nickname>[^@\(\)]+)( \((?P<name>[^@]+)\))?( @ (?P<item>.+))?$")
ABILITY_LINE = re.compile(r"Ability: (?P<ability>.+)$")
EV_LINE = re.compile(r"EVs: [0-9]+ \S+( \/ [0-9]+ \S+)*$")
EV_OR_IV = re.compile(r"(?P<value>[0-9]+) (?P<stat>[^/\s]+)")
NATURE_LINE = re.compile(r"(?P<nature>\S+) Nature$")
IV_LINE = re.compile(r"IVs: [0-9]+ \S+( \/ [0-9]+ \S+)*$")
MOVE_LINE = re.compile(r"- (?P<move>[\S ]+)$")

class Parser:
    @classmethod
    def parse_team(cls, player_id, path):
        team_file = open(path)
        team_text = team_file.read()
        team_text = team_text.strip()
        team_split = [poke.split('\n') for poke in team_text.split('\n\n')]
        finished_team = {}
        for poke in team_split:
            new_poke = Parser.parse_pokemon(player_id, poke)
            finished_team[new_poke.id] = new_poke
        return finished_team

    @classmethod
    def parse_pokemon(cls, player_id, lines):
        name, nickname, nature, item, ability, move_list, ev_dict, iv_dict = None, None, None, None, None, [], {}, {}
        state = 'name' # Start by parsing the name
        for line in lines:
            print(line)
            line_not_parsed = True
            while(line_not_parsed):
                if state is 'name':
                    match_result = NAME_LINE.match(line)
                    match_result = match_result or NICKNAME_LINE.match(line)
                    if match_result is None:
                        raise Exception('This Pokémon has no name')
                    results = match_result.groupdict()
                    name = results['name']
                    nickname = results['nickname'] if 'nickname' in results else results['name']
                    item = results['item']
                    state = 'ability'
                    line_not_parsed = False
                elif state is 'ability':
                    match_result = ABILITY_LINE.match(line)
                    if match_result is None:
                        raise Exception('This Pokémon has no ability')
                    results = match_result.groupdict()
                    ability = results['ability']
                    state = 'evs'
                    line_not_parsed = False
                elif state is 'evs':
                    match_result = EV_LINE.match(line)
                    if match_result is None:
                        state = 'nature'
                        continue
                        # Not raising exception because could
                        # feasibly just not have EVs
                        # raise Exception('This Pokémon has no EVs')
                    results = EV_OR_IV.findall(line)
                    for ev in results:
                        ev_dict[ev[1]] = int(ev[0])
                    state = 'nature'
                    line_not_parsed = False
                elif state is 'nature':
                    match_result = NATURE_LINE.match(line)
                    if match_result is None:
                        raise Exception('This Pokémon has no nature')
                    results = match_result.groupdict()
                    nature = results['nature']
                    state = 'ivs'
                    line_not_parsed = False
                elif state is 'ivs':
                    match_result = IV_LINE.match(line)
                    if match_result is None:
                        state = 'moves'
                        continue
                        # Not raising exception because could
                        # feasibly just not have IVs
                        # raise Exception('This Pokémon has no IVs')
                    results = EV_OR_IV.findall(line)
                    for iv in results:
                        iv_dict[iv[1]] = int(iv[0])
                    state = 'moves'
                    line_not_parsed = False
                elif state is 'moves':
                    match_result = MOVE_LINE.match(line)
                    if match_result is None:
                        raise Exception('This Pokémon has no moves')
                    results = match_result.groupdict()
                    move_list.append(results['move'])
                    line_not_parsed = False
                else:
                    raise Exception('Invalid parse state')
        return pokemon.pokemon.Pokemon(player_id, name, nickname, nature, item, ability, move_list, ev_dict, iv_dict)
