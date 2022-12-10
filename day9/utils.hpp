#ifndef utils_hpp
#define utils_hpp

#include <stdio.h>
#include <vector>
#include <array>

std::vector<std::pair<char, int>> readMoves();

void printMoves(std::vector<std::pair<char, int>> input);
void printCWD();
void printCoords(std::vector<std::array<int, 2>> input);

#endif
