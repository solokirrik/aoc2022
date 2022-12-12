#ifndef point_hpp
#define point_hpp

#include <stdio.h>
#include <string>
#include "map"

struct Point{
    int x;
    int y;
    
    Point(int xin, int yin) {
        x = xin;
        y = yin;
    }
    
    std::string toString();
    
    void moveTo(Point newState);
    
    Point toCoordDiff(char move);
    Point getNextHead(char move);
    Point getNextByParent(Point parentOld, Point parentNew);
};

std::map<std::string, bool> toMap(std::vector<Point> v);
std::map<std::string, bool> intersection(std::vector<Point> v1, std::vector<Point> v2);

#endif
