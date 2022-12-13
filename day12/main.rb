require './day12/bfser.rb'
require './day12/printers'

def part1()
  path = Dir.pwd + "/day12/day12"
  # path = Dir.pwd+"/day12/example"

  file = File.open(path)
  inp = file.readlines.map(&:chomp).map { |x| x.split("") }

  file.close

  start_pos, end_pos = get_start_end(inp)
  puts "Start/End: " + String(start_pos) + " " + String(end_pos)

  matrix = inp.map { |row| row.map { |ch| ch.ord - 'a'.ord } }

  # print_heights(matrix)

  solver = BFSer.new(start_pos, end_pos)
  path = solver.bfs(matrix)

  puts path.length - 1
end

def part2()
  path = Dir.pwd + "/day12/day12"
  # path = Dir.pwd+"/day12/example"

  file = File.open(path)
  inp = file.readlines.map(&:chomp).map { |x| x.split("") }

  file.close

  min_path_len = 2 ** ([42].pack('i').size * 16 - 2) - 1 # max integer value
  _, end_pos = get_start_end(inp)
  matrix = inp.map { |row| row.map { |ch| ch.ord - 'a'.ord } }

  extract_starts(matrix).each { |point|
    solver = BFSer.new(point, end_pos)
    path = solver.bfs(matrix)

    if path.length - 1 > 0 && path.length - 1 < min_path_len
      min_path_len = path.length - 1
    end
  }

  puts min_path_len
end

def extract_starts(matrix)
  points = []

  for r in (0..matrix.length - 1)
    for c in (0..matrix[0].length - 1)
      if matrix[r][c] == 0
        points.push([r, c])
      end
    end
  end

  points
end

def get_start_end(ch_matrix)
  start_pos = [0, 0]
  end_pos = [0, 0]

  (0..ch_matrix.length - 1).each { |i|
    (0..ch_matrix[0].length - 1).each { |j|
      if ch_matrix[i][j] == 'S'
        start_pos = [i, j]
        ch_matrix[i][j] = 'a'
        next
      end
      if ch_matrix[i][j] == 'E'
        end_pos = [i, j]
        ch_matrix[i][j] = 'z'
        next
      end
    }
  }

  [start_pos, end_pos]
end

part1
part2
