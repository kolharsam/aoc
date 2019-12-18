OPERATIONS = ["OR", "AND", "LSHIFT", "NOT", "RSHIFT"]

WIRES = Hash.new

File.readlines('input2').each do |line|
    eq,res = line.strip.split(" -> ")
    eq = eq.split
    res = res.strip
    
    if eq.length == 1
        if eq[0] =~ /[a-zA-Z]/
            WIRES[eq[0]] = 0
            WIRES[res] = eq[0]
        else
            WIRES[res] = eq[0].to_i
        end
    end

    if eq.length == 2
        wire = eq[1]
        if WIRES[wire] == nil
            WIRES[wire] = 0
        else
            WIRES[res] = ~WIRES[wire]
        end
    end

    if eq.length == 3
        wire1 = eq[0]
        wire2 = eq[2]
        operation = eq[1]
       
        if WIRES[wire1] == nil
            WIRES[wire1] = 0
        end

        operand1 = WIRES[wire1]
        operand2 = 0

        if WIRES[wire2] == nil and wire2 =~ /[a-zA-Z]/
            WIRES[wire2] = 0
            operand2 = WIRES[wire2]
        else
            wire2 = wire2.to_i
            operand2 = wire2
        end

        case operation
            when "OR"
                WIRES[res] = operand1 | operand2
            when "AND"
                WIRES[res] = operand1 & operand2
            when "LSHIFT"
                WIRES[res] = operand1 << operand2
            when "RSHIFT"
                WIRES[res] = operand1 >> operand2
        end
    end
end

puts WIRES

def get_res (key)
    if WIRES[key].is_a? Integer
        return WIRES[key]
    else
        get_res(WIRES[key])
    end
end

puts get_res("i")