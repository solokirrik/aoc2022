#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <array>
#include <map>
#include <cmath>

#include "utils.hpp"
#include "part1.hpp"

struct Point{
    int x;
    int y;
    
    Point(int xin, int yin) {
        x = xin;
        y = yin;
    }
    
    std::string toString() {
        return std::to_string(x) +"-"+ std::to_string(y);
    }
};

Point toCoordDiff(char move) {
    switch (move) {
        case 'R':
            return {0, 1};
            break;
        case 'L':
            return {0, -1};
            break;
        case 'U':
            return {1, 0};
            break;
        case 'D':
            return {-1, 0};
            break;
        default:
            return {0, 0};
            break;
    }
}

Point getNextHead(Point currHead, char move) {
    Point diffHead = toCoordDiff(move);

    return {currHead.x + diffHead.x, currHead.y + diffHead.y};
}

Point getNextTail(Point currTail, Point oldHead, Point newHead) {
    if (pow(currTail.x - newHead.x, 2) +
             pow(currTail.y - newHead.y, 2) > 2) {
        return oldHead;
    }

    return currTail;
}

std::map<std::string, bool> toMap(std::vector<Point> v) {
    std::map<std::string, bool> out;
    
    for (int i = 0; i < v.size(); i++) {
        out[v[i].toString()] = true;
    }
    
    return out;
}

std::map<std::string, bool> intersection(std::vector<Point> v1, std::vector<Point> v2){
    std::map<std::string, bool> v1Map = toMap(v1);
    std::map<std::string, bool> v2Map = toMap(v2);
    std::map<std::string, bool> v3;
    
    for (auto&& [first, _] : v1Map) {
        if (!v2Map[first]) {
            continue;
        }
        
        v3[first] = true;
    }

    return v3;
}

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
            Point nextHead = getNextHead(currHead, moves[i].first);

            headMoves.emplace_back(nextHead);

            if (i > 0) {
                Point currTail = tailMoves[tailMoves.size()-1];
                Point nextTail = getNextTail(currTail, currHead, nextHead);

                tailMoves.emplace_back(nextTail);
            }
        }
    }

    std::map<std::string, bool> inter3 = intersection(headMoves, tailMoves);
    
    std::cout << "headMoves " << headMoves.size() << "\n";
    std::cout << "tailMoves " << tailMoves.size() << "\n";
    std::cout << "intersection " << inter3.size() << "\n";
}
