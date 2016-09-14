// TeamParser.cpp
// Jacob Ginsparg, Philip Blair
// 9/11/2016

#include <regex>
#include <stdexcept>

#include "Ability.h"
#include "EffortValue.h"
#include "IndividualValue.h"
#include "Move.h"
#include "TeamParser.h"
#include "Type.h"

using namespace pokemon_sim;

const std::regex NAME_LINE = std::regex("([^@]+)(?: @ (.+))?");
const std::regex ABILITY_LINE = std::regex("Ability: (.+)$");
const std::regex EV_LINE = std::regex("EVs: [0-9]+ [^[:space:]]+(?: / [0-9]+ [^[:space:]]+)*");
const std::regex EV_OR_IV = std::regex("([0-9+]) ([^[:space:]]+)");
const std::regex NATURE_LINE = std::regex("([^[:space:]]+) Nature$");
const std::regex IV_LINE = std::regex("IVs: [0-9]+ [^[:space:]]+(?: / [0-9]+ [^[:space:]]+)*");
const std::regex MOVE_LINE = std::regex("- ([^[:space:]]+)");

enum parse_state {
  NAME,
  ABILITY,
  EV,
  NATURE,
  IV,
  MOVES
};

Pokemon *parse_pokemon(std::fstream &team_file) {
  std::smatch sm;
  parse_state state = NAME;
  std::string line;
  std::string name;
  std::string item;
  std::string nature;
  std::string ability;
  EffortValue evs;
  IndividualValue ivs;
  std::vector<Move> moves = std::vector<Move>();

  bool started = false;

  while (std::getline(team_file, line)) {
    if (line.length() == 0) {
      if (!started) {
        return NULL;
      } else {
        break; // While loop
      }
    }
    switch (state) {
    case NAME:
      if (!std::regex_match(line, sm, NAME_LINE)) {
        throw std::runtime_error("This Pokemon has no name");
      }
      name = sm[1];
      item = sm[2];
      started = true;
      state = ABILITY;
      break;
    case ABILITY:
      if (!std::regex_match(line, sm, ABILITY_LINE)) {
        throw std::runtime_error("This Pokemon has no ability");
      }
      ability = sm[1];
      state = EV;
      break;
    case EV:
      if (std::regex_match(line, sm, EV_LINE)) {
        std::map<std::string, int> ev_map;
        for(std::sregex_iterator i = std::sregex_iterator(line.begin(), line.end(), EV_OR_IV);
                            i != std::sregex_iterator();
                            ++i ) {
          sm = *i;
          // e.g. "HP", "12"
          ev_map[sm[2]] = stoi(sm[1]);
        }
        evs = EffortValue(ev_map);
      }
      state = NATURE;
      break;
    case NATURE:
      if (std::regex_match(line, sm, NATURE_LINE)) {
        nature = sm[1];
      }
      state = IV;
      break;
    case IV:
      if (std::regex_match(line, sm, IV_LINE)) {
        std::map<std::string, int> iv_map;
        for(std::sregex_iterator i = std::sregex_iterator(line.begin(), line.end(), EV_OR_IV);
                            i != std::sregex_iterator();
                            ++i ) {
          sm = *i;
          iv_map[sm[2]] = stoi(sm[1]);
        }
        ivs = IndividualValue(iv_map);
      }
      state = MOVES;
      break;
    case MOVES:
      if (!std::regex_match(line, sm, MOVE_LINE)) {
        throw std::runtime_error("This pokemon has no moves");
      }
      moves.push_back(Move(sm[1]));
      break;
    default:
      throw std::runtime_error("This shouldn't ever display");
    }
  }
  Pokemon poke = Pokemon(name, nature, item, ability, evs, ivs, moves);
  Pokemon *p_poke = &poke;
  return p_poke;
}

std::vector<Pokemon> parse_team(std::fstream team_file) {
  std::vector<Pokemon> ret = std::vector<Pokemon>();
  Pokemon *poke = parse_pokemon(team_file);
  while (poke) {
    ret.push_back(*poke);
    poke = parse_pokemon(team_file);
  }
  return ret;
}
