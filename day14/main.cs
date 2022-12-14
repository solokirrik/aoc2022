using day14;

const char stone = '#';
const char sand = 'o';
const int inX = 500;
const int inY = 0;

const string path = @"../../../example";
//const string path = @"../../../day14";

Part1();
Part2();

static void Part1()
{
    PourSand(GetInput(false));
}


static void Part2()
{
    PourSand(GetInput(true));
}

static void PourSand(Cave cave)
{
    var grainsCount = 0;
    var done = false;

    while (!done)
    {
        cave.Print();
        
        var grainPos = new CavePoint(inX, inY);

        while (true)
        {
            if (cave.IsFree(grainPos.X, grainPos.Y + 1))
            {
                grainPos.Y++;
                if (cave.IsOutOfBox(grainPos.X, grainPos.Y))
                {
                    done = true;
                    break;
                }

                continue;
            }

            if (cave.IsFree(grainPos.X - 1, grainPos.Y + 1))
            {
                grainPos.Y++;
                grainPos.X--;
                if (cave.IsOutOfBox(grainPos.X, grainPos.Y))
                {
                    done = true;
                    break;
                }

                continue;
            }

            if (cave.IsFree(grainPos.X + 1, grainPos.Y + 1))
            {
                grainPos.Y++;
                grainPos.X++;
                if (cave.IsOutOfBox(grainPos.X, grainPos.Y))
                {
                    done = true;
                    break;
                }

                continue;
            }
            
            if (cave.IsOutOfBox(grainPos.X, grainPos.Y))
            {
                done = true;
                break;
            }

            grainsCount++;
            cave.AddPoint(grainPos.X, grainPos.Y, sand);
            
            if (grainPos.X == inX && grainPos.Y == inY)
            {
                done = true;
            }
            
            break;
        }
    }

    Console.WriteLine("GrainsCount: {0}", grainsCount);
}


static Cave GetInput(bool isPart2)
{
    var caveMap = new Cave();

    var counter = 0;
    var upperLeft = new CavePoint(Int32.MaxValue, 0);
    var lowerRight = new CavePoint(Int32.MinValue, Int32.MinValue);
    
    foreach (var line in System.IO.File.ReadLines(path))
    {
        var rockEdges = line.Split(" -> ");
        var lastPair = new CavePoint(0, 0);

        for (var i = 0; i < rockEdges.Length; i++)
        {
            var coordPair = rockEdges[i].Split(",");
            var x = int.Parse(coordPair[0]);
            var y = int.Parse(coordPair[1]);

            upperLeft.X = x < upperLeft.X ? x : upperLeft.X;
            upperLeft.Y = y < upperLeft.Y ? y : upperLeft.Y;
            lowerRight.X = x > lowerRight.X ? x : lowerRight.X;
            lowerRight.Y = y > lowerRight.Y ? y : lowerRight.Y;

            caveMap.AddPoint(x, y, stone);
            if (i == 0)
            {
                lastPair.X = x;
                lastPair.Y = y;
               
                continue;
            }

            if (x != lastPair.X)
            {
                var minX = Math.Min(lastPair.X, x);
                var countX = Math.Max(lastPair.X, x) - minX;
                
                foreach (var xi in Enumerable.Range(minX, countX))
                {
                    caveMap.AddPoint(xi, y, stone);
                }
            }

            if (y != lastPair.Y)
            {
                var minY = Math.Min(lastPair.Y, y);
                var countY = Math.Max(lastPair.Y, y) - minY;
                
                foreach (var yi in Enumerable.Range(minY, countY))
                {
                    caveMap.AddPoint(x, yi, stone);
                }
            }

            lastPair.X = x;
            lastPair.Y = y;
        }

        counter++;
    }

    if (isPart2)
    {
        lowerRight.Y+=2;
        lowerRight.X += 1000;
        upperLeft.X -= 1000;
        
        for (var xi = upperLeft.X; xi <= lowerRight.X; xi++)
        {
            caveMap.AddPoint(xi, lowerRight.Y, stone);
        }
    } 

    Console.WriteLine("There were {0} lines.", counter.ToString());
    Console.WriteLine("Rock parts: {0}", caveMap);

    caveMap.SetBoundaries(upperLeft, lowerRight);

    return caveMap;
}