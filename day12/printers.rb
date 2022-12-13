def get_empty_mtx(ch_matrix)
  ch_mtx = []

  (0..ch_matrix.length - 1).each { |i|
    ch_mtx.append(['.'] * ch_matrix[0].length)
  }

  ch_mtx
end

def print(ch_matrix, r, c)
  ch_mtx = get_empty_mtx(ch_matrix)
  puts String(r) + " " + String(c)

  if r >= 0 && r < ch_matrix.length && c >= 0 && c < ch_matrix[0].length
    (ch_mtx[r][c] = 'o')
  end

  (0..ch_matrix.length - 1).each { |i|
    puts ch_mtx[i].join("")
  }

  puts "\n"
end

def print_heights(matrix)
  (0..matrix.length - 1).each { |i|
    puts matrix[i].join("\t")
  }

  puts "\n"
end
