/* -*- C++ -*- */
// Pokemon.h
// Jacob Ginsparg
// 7/9/2016

#ifndef _POKEMON_H
#define _POKEMON_H

#include <string>
#include <vector>
#include "Type.h"
#include "Move.h"
#include "Ability.h"
#include "EffortValue.h"
#include "IndividualValue.h"


namespace pokemon_sim {
  class Pokemon {
    // Private Properties
    EffortValue ev;
    IndividualValue iv;
  public:
    // Properties
    std::string name;
    std::string nature;
    std::string item;
    Ability* ability;
    std::vector<Type> types;
    std::vector<Move> moveset;
    int hp;
    int atk;
    int def;
    int spa;
    int spd;
    int spe;

    // Constructor
    Pokemon(std::string name, std::string nature, std::string item,
      std::string ability, EffortValue evs, IndividualValue ivs, std::vector<Move> moves);
  };
}
#endif
