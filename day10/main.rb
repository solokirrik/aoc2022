path = "./day10"

file = File.open(path)
file_data = file.readlines.map(&:chomp)
file.close

def log(mark, cycle, x, performance)
  data = { c: cycle, x: x, val: x * cycle, p: performance }
  puts mark + String(data)
end

# 17380
def part1(inp)
  x = 1
  cycle = 1
  perf_cycle = 20
  performance = 0

  inp.each { |cmd|
    if cycle == perf_cycle
      performance += x * cycle
      perf_cycle += 40
    end

    if cmd == 'noop'
      cycle += 1
      next
    end

    if cmd.start_with?("addx")
      cycle += 1
      if cycle == perf_cycle
        perf_cycle += 40
        performance += x * cycle
      end
      cycle += 1
      x += Integer(cmd[5, cmd.length])
    end
  }

  puts performance
end

def part2

end

part1(file_data)
part2()
