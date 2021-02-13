numbers = [2,5,7,9,3,10,23]

# Append
numbers.append(32)
print(numbers)

#Insert
numbers.insert(0,7)
print(numbers)

#Remove
numbers.remove(9)
print(numbers)

#Clear
numbers.clear()
print(numbers)

#Pop
numbers = [2,5,7,9,3,5]

numbers.pop()
print(numbers)

#Index
print(numbers.index(9))

#In operator

print (50 in numbers) # TO CHECK EXISTING ITEM IN THE LIST LIKE INDEX METHOD.. IT WILL RETURN BOOLEAN VALUE.

#Count
numbers = [2,5,7,9,3,5]
print(numbers.count(5)) #TO COUNT THE REPEATED NUMBERS IN THE LIST

#SORT
numbers.sort()
print(numbers)

#REVERSE

numbers.reverse()
print(numbers)

#COPY

numbers2 = numbers.copy()
numbers.append(60)
print(numbers2)


#EXERCISE

numbers = [2,8,6,7,6,8,2,5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
