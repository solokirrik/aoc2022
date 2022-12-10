#ifndef rope_hpp
#define rope_hpp

#include <stdio.h>
#include <vector>

#include "point.hpp"

struct Rope {
    std::vector<Point> knots;
    
    Rope(int knotsCount) {
        this->knots.reserve(knotsCount);
        
        for (int i = 0; i < knotsCount; i++) {
            this->knots.emplace_back(Point(0,0));
        }
    }
    
    void moveHead(char move);
    void moveBody();
    void moveIt(char move);
    void moveIt2(char move);
};

void printRope(Rope input);
void drawRope(Rope rope);

#endif
