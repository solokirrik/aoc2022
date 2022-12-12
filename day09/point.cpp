#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cmath>

#include "point.hpp"


std::string Point::toString() {
    return std::to_string(x) +"/"+ std::to_string(y);
}

void Point::moveTo(Point newState) {
    this->x = newState.x;
    this->y = newState.y;
}

Point Point::getNextHead(char move) {
    if (move == 'R') {
        this->x++;
    } else if (move == 'L') {
        this->x--;
    } else if (move == 'U') {
        this->y++;
    } else if (move == 'D') {
        this->y--;
    }

    return *this;
}

Point Point::getNextByParent(Point parentOld, Point parentNew) {
    if (pow(this->x - parentNew.x, 2) +
        pow(this->y - parentNew.y, 2) > 2) {
        return parentOld;
    }

    return *this;
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

void printCoords(std::vector<Point> input) {
    for (int i = 0; i < input.size(); i++) {
        std::cout << input.at(i).x << '-' << input.at(i).y << ' ';
    }
    
    std::cout << '\n';
}
