#include <iostream>
#include <vector>
#include <string>
#include <map>

#include "utils.hpp"
#include "part1.hpp"
#include "point.hpp"


void part1() {
    std::vector<std::pair<char, int>> moves = readMoves();
    
    std::vector<Point> headMoves;
    std::vector<Point> tailMoves;
    
    headMoves.reserve(moves.size());
    tailMoves.reserve(moves.size());
    
    headMoves.emplace_back(Point(0,0));
    tailMoves.emplace_back(Point(0,0));
    
    for (int i = 0; i < moves.size(); i++) {
        for (int j = 0; j < moves[i].second; j++){
            Point currHead = headMoves[headMoves.size()-1];
            Point nextHead = currHead.getNextHead(moves[i].first);
            
            headMoves.emplace_back(nextHead);
            
            if (i > 0) {
                Point currTail = tailMoves[tailMoves.size()-1];
                Point nextTail = currTail.getNextByParent(currHead, nextHead);
                
                tailMoves.emplace_back(nextTail);
            }
        }
    }
    
    std::map<std::string, bool> inter3 = intersection(headMoves, tailMoves);
    
    std::cout << "headMoves " << headMoves.size() << "\n";
    std::cout << "tailMoves " << tailMoves.size() << "\n";
    std::cout << "intersection " << inter3.size() << "\n";
}
