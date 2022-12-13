input_data = []
s1 = ''
s2 = ''
result = 0

alfa = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a_dict = dict([(x[1], x[0]+1) for x in enumerate(alfa)])

with open('puzzle3_input.txt', 'r') as file:
    for line in file:
        input_data = list(line.strip())

        s1 = input_data[:len(input_data)//2]
        s2 = input_data[len(input_data)//2:]

        for i in s1:
            if i in s2:
                result += int(a_dict[i])
                break
                
print(result)
