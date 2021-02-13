names =["Prachi","sukanya","shruti","Ashish","Sagar"]
print(names)
print(names[0])
print(names[3])
print(names[-1])
print(names[2:])
print(names[2:4]) #it will return upto index -1 value i.e 4-1 = 3 upto ashish

# you can set new elements
names[0]= "Avinash"
print(names)

#Find the largest number in list

numbers = [2,5,7,4,8,12]
max = numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)


#2D List

matrix = [
    [1,2,3] ,#index [0]
    [4,5,6] ,#index[1]
    [7,8,9] #index[2]
]

for row in matrix:
   for item in row:
      print(item)



print(matrix[1][1])
print(matrix[2][2])
print(matrix[1][2])