'''for X in range(4):
    for Y in range(3):
        print(f'({X},{Y})')


numbers =[5,2,5,2,2]
for x_counts in numbers:
   # print("X" * x_counts)
    output =""
    for count in range(x_counts):
        output += 'X'
    print(output)

'''

numbers =[2,2,2,2,7,7]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += 'X'
    print(output)
