namespace day14;

public class CavePoint
{
    public int X { get; set; }
    public int Y { get; set; }

    public CavePoint(int x, int y)
    {
        X = x;
        Y = y;
    }

    public override int GetHashCode()
    {
        int hash = 23;

        hash = hash * 31 + X;
        hash = hash * 31 + Y;

        return hash;
    }

    public override bool Equals(object? obj)
    {
        return Equals(obj as CavePoint);
    }

    bool Equals(CavePoint? obj)
    {
        return obj != null && obj.X == X && obj.Y == Y;
    }
};