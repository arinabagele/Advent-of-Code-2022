
result = 0
with open('puzzle2_input.txt', 'r') as file:
    # Rock:     A   X (1)
    # Paper:    B   Y (2)
    # Scissors: C   Z (3)
    #won: 6
    #lost: 0
    #draw: 3
    for line in file:
        l = line.strip()
        
        if l[-1] == 'X':
            result += 1
        elif l[-1] == 'Y':
            result += 2
        else:
            result += 3
        
        # winning combinations
        if l in ['A Y', 'C X', 'B Z']:
            result += 6

        # draw combinations
        elif l in ['A X', 'B Y', 'C Z']:
            result += 3

        else:
            result += 0

print(result)
