require 'json'

file = File.open("8.in")
file_data = file.readlines.map(&:chomp)

# part 1
p1 = file_data.reduce(0) { |diff, val|
  diff + (val.length - eval(val).length)
}

puts p1

# part 2

p2 = file_data.reduce(0) { |diff, val|
  diff + JSON.generate(val).length - val.length
}

puts p2

file.close
