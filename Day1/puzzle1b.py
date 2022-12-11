max_numbers = []
s = 0

with open('puzzle1_input.txt', 'r') as file:

    for line in file:
        if len(line) > 1:
            s += int(line)

        elif len(line) <= 1 or file.readline() == "":
            if len(max_numbers) < 3:
                max_numbers.append(s)

            else:
                if s > min(max_numbers):
                    max_numbers.pop(max_numbers.index(min(max_numbers)))
                    max_numbers.append(s)

            s = 0

    print(sum(max_numbers))
