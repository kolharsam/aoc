file = File.open("input")
file_data = file.readlines.map(&:chomp)

require 'set'
chars = file_data[0].split('')
unique_houses = Set.new

x = 0
y = 0

chars.each { |char|
    if char == '^'
        y += 1   
    elsif char == '>'
        x += 1 
    elsif char == '<'
        x -= 1
    elsif char == 'v'
        y -= 1
    end
    unique_houses.add([x, y])
}

puts unique_houses.length  # PART 1 

unique_houses.clear # to empty the current set

san_x = 0
san_y = 0
rob_x = 0
rob_y = 0
x = 0
y = 0

t = true
unique_houses.add([0,0])

chars.each { |char|        
    if char == '^'
        y += 1   
    elsif char == '>'
        x += 1 
    elsif char == '<'
        x -= 1
    elsif char == 'v'
        y -= 1
    end

    if t == true
        t = false
        san_x += x
        san_y += y
        unique_houses.add([san_x, san_y])
    else
        t = true
        rob_x += x
        rob_y += y
        unique_houses.add([rob_x, rob_y])
    end

    x = 0
    y = 0
}

puts unique_houses.length # part 2

file.close