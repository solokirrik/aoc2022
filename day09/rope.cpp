#include <array>
#include <iostream>
#include <vector>
#include <limits>
#include <cmath>

#include "rope.hpp"
#include "point.hpp"


void Rope::moveIt(char move) {
    Point oldHead = this->knots[0];
    Point oldParent = oldHead;

    Point newHead = oldHead.getNextHead(move);
    
    this->knots[0] = newHead;
    
    for (int i = 1; i < this->knots.size(); i++ ) {
        Point currState = this->knots[i];
        
        Point nextState = currState.getNextByParent(oldParent, this->knots[i-1]);
        
        this->knots[i].moveTo(nextState);
        
        oldParent = currState;
    }
}

void Rope::moveIt2(char move) {
    this->moveHead(move);
    this->moveBody();
}

void Rope::moveHead(char move) {
    this->knots[0] = this->knots[0].getNextHead(move);
}

void Rope::moveBody() {
    for (int i = 1; i < this->knots.size(); i++ ) {
        int deltaX = this->knots[i-1].x - this->knots[i].x;
        int deltaY = this->knots[i-1].y - this->knots[i].y;

        if (pow(deltaX, 2) + pow(deltaY, 2) <= 2) {
            return;
        }

        if (deltaY > 0) {
            this->knots[i].y++;
        }
        if (deltaY < 0) {
            this->knots[i].y--;
        }
        if (deltaX > 0) {
            this->knots[i].x++;
        }
        if (deltaX < 0) {
            this->knots[i].x--;
        }
    }
}


void printRope(Rope input) {
    for (int i = 0; i < input.knots.size(); i++) {
        std::cout << input.knots.at(i).x << '-' << input.knots.at(i).y << ' ';
    }
    
    std::cout << '\n';
}

void drawRope(Rope rope) {
    int minX = -15;
    int maxX = 15;
    int minY = -15;
    int maxY = 15;
    
    std::vector<char> row;
    std::vector<std::vector<char>> matrix;

    for (int j = 0; j <  maxX-minX+1; j++){
        row.emplace_back('.');
    }

    for (int i = 0; i < maxY-minY+1; i++) {
        matrix.emplace_back(row);
    }

    for (int i = 0; i < rope.knots.size(); i++) {
        int x = rope.knots[i].x - minX;
        int y = rope.knots[i].y - minY;

        matrix[y][x] = i + '0';
    }

    for (int r = 0; r < matrix.size(); r++){
        for (int c = 0; c < matrix[0].size(); c++) {
            std::cout << matrix[r][c];
        }
        
        std::cout << '\n';
    }
}
