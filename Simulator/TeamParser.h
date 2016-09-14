/* -*- C++ -*- */
// TeamParser.h
// Jacob Ginsparg, Philip Blair
// 9/11//2016

#ifndef _POKEMON_SIM_TEAM_PARSER_H
#define _POKEMON_SIM_TEAM_PARSER_H

#include <fstream>
#include <vector>

#include "Pokemon.h"

namespace pokemon_sim {
  std::vector<Pokemon> parse_team(std::fstream team_file);
}

#endif
