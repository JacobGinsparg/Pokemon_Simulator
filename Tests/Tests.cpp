// Tests.cpp
// Jacob Ginsparg
// 9/12/2016

#include <fstream>
#include <iostream>

#include "TeamParser.h"
#include "Tests.h"

using namespace pokemon_sim;

int main(int argc, char const *argv[]) {
  std::string line;
  std::ifstream team_file("NewOU.txt");
  if (team_file.is_open()) {
    while (getline(team_file, line)) {
      std::cout << line << "\n";
    }
    team_file.close();
  } else {
    std::cout << "Unable to open file" << std::endl;
  }
  return 0;
}
