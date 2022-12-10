#ifndef utils_hpp
#define utils_hpp

#include <stdio.h>
#include <vector>
#include <array>

#include "point.hpp"

std::vector<std::pair<char, int>> readMoves();

void printMoves(std::vector<std::pair<char, int>> input);
void printCWD();

#endif
