#include <iostream>
#include <vector>
#include <array>
#include <fstream>

#include "utils.hpp"
#include "point.hpp"
#include "rope.hpp"

std::vector<std::pair<char, int>> readMoves() {
    std::string mystring;
    std::ifstream myfile;
    std::vector<std::pair<char, int>> moves;
    
    myfile.open("./day9.txt");
    
    if (!myfile.is_open())  {
        std::cout << "unable to read file" << '\n';
        
        return moves;
    }
    
    while (getline(myfile, mystring)) {
        long pos = mystring.find(" ");
        char move = mystring.substr(0, pos)[0];
        int dist = stoi(mystring.substr(pos+1,mystring.length()));
        
        moves.emplace_back(move, dist);
    }
    
    myfile.close();
    
    return moves;
}

void printMoves(std::vector<std::pair<char, int>> input) {
    for (int i = 0; i < input.size(); i++) {
        std::cout << input.at(i).first << '-' << input.at(i).second << ' ';
    }
    
    std::cout << '\n';
}

void printCWD() {
    std::filesystem::path cwd = std::filesystem::current_path();
    std::ofstream file(cwd.string());
    file.close();
    
    std::cout << cwd.string();
}
