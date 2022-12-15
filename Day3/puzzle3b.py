
alfa = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a_dict = dict([(x[1], x[0]+1) for x in enumerate(alfa)])

input_data = []
result = 0
lis_l = []
i = 0

with open('puzzle3_input.txt', 'r') as file:
    input_data = [line.strip() for line in file]

    while i in range(len(input_data)):
        list_l = input_data[i:i+3]

        for l in list_l[0]:
            if l in list_l[0] and l in list_l[1] and l in list_l[2]:
                result += a_dict[l]
                break

        list_l = []
        i += 3

print(result)
