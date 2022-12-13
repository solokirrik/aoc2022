class BFSer
  @visited = {}
  @start = [0, 0]
  @end = [0, 0]

  def initialize(start_pos, end_pos)
    @visited = {}
    @start = start_pos
    @end = end_pos
  end

  def bfs(matrix)
    connections = {}
    queue = [@start]
    @visited[@start] = true
    found = false

    while queue.length > 0
      point = queue.shift

      if point == @end
        found = true
        break
      end

      for neighbour in available_neighbours(matrix, point)
        if @visited.include?(neighbour)
          next
        end

        @visited[neighbour] = true
        queue.push(neighbour)
        connections[neighbour] = point
      end
    end

    path = []
    curr_position = @end.dup

    if found
      path.push(curr_position)

      until connections[curr_position].nil?
        loc_parent = connections[curr_position]
        path.push(loc_parent)
        curr_position = connections[curr_position]
      end

      path.reverse
    end

    path
  end
end

def available_neighbours(matrix, point)
  neighbours = []
  rows = matrix.length
  columns = matrix[0].length

  [[-1, 0], [1, 0], [0, -1], [0, 1]].each { |n|
    p_row = point.at(0)
    p_col = point.at(1)
    n_row = n.at(0)
    n_col = n.at(1)

    if p_row + n_row >= 0 and p_row + n_row < rows and
      p_col + n_col >= 0 and p_col + n_col < columns and
      matrix[p_row + n_row][p_col + n_col] <= 1 + matrix[p_row][p_col]
      neighbours.push([p_row + n_row, p_col + n_col])
    end
  }

  neighbours
end
