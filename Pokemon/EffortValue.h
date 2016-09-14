/* -*- C++ -*- */
// EffortValue.h
// Jacob Ginsparg
// 9/11/2016

#ifndef _POKEMON_SIM_EV_H
#define _POKEMON_SIM_EV_H

#include <map>
#include <string>

namespace pokemon_sim {
  class EffortValue {
  public:
    EffortValue();
    EffortValue(std::map<std::string, int> const ev_map);
  };
}

#endif
