#include <stdio.h>
#include <iostream>
#include <vector>
#include <unistd.h>

#include "part2.hpp"
#include "point.hpp"
#include "rope.hpp"
#include "utils.hpp"

int KNOTS_COUNT = 10;
int SECOND = 1000000;


void debugDraw(Rope rope) {
    std::cout << "\n\n";
    
    drawRope(rope);
    
    usleep(0.1*SECOND);
}


Point getLast(std::vector<Point> v) {
    return v[v.size()-1];
}

Point getFirst(std::vector<Point> v) {
    return v[v.size()-1];
}

struct Logger {
    std::vector<Point> headMoves;
    std::vector<Point> tailMoves;

    void write(Rope rope) {
        Point currHead = rope.knots[0];
        Point currTail = getLast(rope.knots);
        
        if (headMoves.size() == 0 || tailMoves.size() == 0 ) {
            headMoves.emplace_back(currHead);
            tailMoves.emplace_back(currTail);
        }
        
        Point lastHead = getLast(headMoves);
        Point lastTail = getLast(tailMoves);
        
        if (lastHead.x != currHead.x || lastHead.y != currHead.y) {
            headMoves.emplace_back(currHead);
        }

        if (lastTail.x != currTail.x || lastTail.y != currTail.y) {
            tailMoves.emplace_back(currTail);
        }
    }
};

void part2() {
    std::vector<std::pair<char, int>> moves = readMoves();
    
    Rope rope = Rope(KNOTS_COUNT);
    
    Logger log;
    log.write(rope);
    
    for (int i = 0; i < moves.size(); i++) {
        for (int j = 0; j < moves[i].second; j++){
            rope.moveIt2(moves[i].first);
            log.write(rope);
            debugDraw(rope);
        }
    }

    std::cout << "headMoves:\t" << log.headMoves.size() << "\n";
    std::cout << "tailMoves:\t" << log.tailMoves.size() << "\n";
    std::cout << "intersection:\t" << intersection(log.headMoves, log.tailMoves).size() << "\n";
    std::cout << "unique tail:\t" << toMap(log.tailMoves).size() << "\n";
}
