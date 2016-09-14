/* -*- C++ -*- */
// IndividualValue.h
// Jacob Ginsparg
// 9/11/2016

#ifndef _POKEMON_SIM_IV_H
#define _POKEMON_SIM_IV_H value

#include <map>
#include <string>

namespace pokemon_sim {
  class IndividualValue {
  public:
    IndividualValue();
    IndividualValue(std::map<std::string, int> const iv_map);
  };
}

#endif
