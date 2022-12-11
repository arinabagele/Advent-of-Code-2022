max_number = 0
sum = 0

with open('puzzle1_input.txt', 'r') as file:

    for line in file:
        if len(line) > 1:
            sum += int(line)

        elif len(line) <= 1 or file.readline() == "":
            if max_number < sum:
                max_number = sum

            sum = 0

    print(max_number)
