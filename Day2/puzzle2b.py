
result = 0


def change_letter(a):
    match a:
        case 'A X':
            return 'A Z'
        case 'A Y':
            return 'A X'
        case 'A Z':
            return 'A Y'

        case 'B X':
            return 'B X'
        case 'B Y':
            return 'B Y'
        case 'B Z':
            return 'B Z'

        case 'C X':
            return 'C Y'
        case 'C Y':
            return 'C Z'
        case 'C Z':
            return 'C X'


with open('puzzle2_input.txt', 'r') as file:
    # Rock:     A   X (1)
    # Paper:    B   Y (2)
    # Scissors: C   Z (3)
    #won: 6  (Z)
    #lost: 0 (X)
    #draw: 3 (Y)
    for line in file:
        l = change_letter(line.strip())
        if l[-1] == 'X':
            result += 1
        elif l[-1] == 'Y':
            result += 2
        else:
            result += 3

        # won combinations: Paper-Rock, Rock-Scissors, Scissors-Paper
        if l in ['A Y', 'C X', 'B Z']:
            result += 6

        # draw combinations: Paper-Rock, Rock-Scissors, Scissors-Paper
        elif l in ['A X', 'B Y', 'C Z']:
            result += 3

        else:
            result += 0


print(result)
