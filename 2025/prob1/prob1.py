import sys

input_file = ""

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = "input.example"

max_nums = 99

def read_input():
    file = open(input_file, "r")
    return file.read().strip().split("\n")

def p1():
    lines = read_input()
    times_zero = 0
    start = 50

    for line in lines:
        direction, value = line[0], line[1:]
        value = int(value)

        if direction == "R":
            start = (start + value) % (max_nums + 1) # move right circularly
        elif direction == "L":
            start = (start - value) % (max_nums + 1) # move left circularly
        print(start, direction, value)

        if start == 0:
            times_zero += 1
    
    print("Times at zero:", times_zero)

def p2():
    lines = read_input()
    times_zero = 0
    current_position = 50
    NUM_POSITIONS = 100

    for line in lines:
        if not line:
            continue

        direction, value_str = line[0], line[1:]
        value = int(value_str)
        
        previous_position = current_position
        total_clicks_at_zero = 0

        if direction == "R":
            # RIGHT: We hit 0 every time the total value crosses a multiple of 100.
            # (Start + Distance) // 100
            total_clicks_at_zero = (previous_position + value) // NUM_POSITIONS
            
            # Update Position
            current_position = (previous_position + value) % NUM_POSITIONS

        elif direction == "L":
            # LEFT: Logic depends on whether we start at 0 or not.
            
            if previous_position == 0:
                # If we start at 0 and move Left, we go to 99 immediately.
                # We only hit 0 again if we rotate a full 100 times.
                total_clicks_at_zero = value // NUM_POSITIONS
            else:
                # If we are not at 0, we hit 0 if the rotation is >= current position.
                if value < previous_position:
                    total_clicks_at_zero = 0
                else:
                    # We hit 0 once (to get to 0), plus any full loops (100s) after that.
                    # remaining_value = value - previous_position
                    total_clicks_at_zero = 1 + (value - previous_position) // NUM_POSITIONS

            current_position = (previous_position - value) % NUM_POSITIONS
            if current_position < 0:
                 current_position += NUM_POSITIONS

        times_zero += total_clicks_at_zero

    print("Times at zero:", times_zero)

if __name__ == "__main__":
    p1()
    p2()
