// Pokemon.h
// Jacob Ginsparg
// 7/9/2016

#ifndef __POKEMON_H__
#define __POKEMON_H__

#include <Type.h>
#include <Ability.h>
using namespace std;

class Pokemon {
  // Private Properties
  int baseHp, baseAtk, baseDef, baseSpa, baseSpd, baseSpe;
  EffortValue ev;
  IndividualValue iv;
public:
  // Properties
  string name;
  Type[] types;
  Ability ability;
  int weight;
  Move[] moveset;

  // Constructors and factories
  Pokemon();
  Pokemon(string);
  static Pokemon parsePokemon(string);

  // Functions
  int hp();
  int atk();
  int def();
  int spa();
  int spd();
  int spe();
};

#endif
