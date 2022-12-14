namespace day14;

public class Cave
{
    private Dictionary<CavePoint, char> Store = new();
    private CavePoint UpperLeft;
    private CavePoint LowerRight;

    public void SetBoundaries(CavePoint upperLeft, CavePoint lowerRight)
    {
        UpperLeft = upperLeft;
        LowerRight = lowerRight;
    }

    public void AddPoint(int x, int y, char val)
    {
        Store[new CavePoint(x, y)] = val;
    }

    public bool IsOutOfBox(int x, int y)
    {
        return x < UpperLeft.X || x > LowerRight.X ||
               y < 0 || y > LowerRight.Y;
    }

    public bool IsFree(int x, int y)
    {
        return !Store.ContainsKey(new CavePoint(x, y));
    }

    public void Print()
    {
        var minX = UpperLeft.X;
        var minY = UpperLeft.Y;

        var maxX = LowerRight.X;
        var maxY = LowerRight.Y;

        var mtx = new List<List<char>>();
        for (var r = minY; r <= maxY; r++)
        {
            var row = new List<char>();
            for (var c = minX - minX; c <= maxX - minX; c++)
            {
                row.Add('.');
            }

            mtx.Add(row);
        }

        foreach (var point in Store)
        {
            var y = point.Key.Y;
            var x = point.Key.X - minX;

            mtx[y][x] = point.Value;
        }

        for (var r = minY; r <= maxY; r++)
        {
            Console.WriteLine(String.Join("", mtx[r]));
        }
        Console.WriteLine("\n\n");
    }
}
