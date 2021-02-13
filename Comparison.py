temperature = 5
if temperature>30:
    print("It's a hot day")
elif temperature<10:
    print("It's a cold day")
else:
    print("it's neither hot nor cold")

#Exercise

name = "Sagar Hedaoo"
if len(name)< 3:
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Name can be a maximum of 50 characters")
else:
    print("name looks Good..!!")

# Exercise:
weight = int(input("Weight :"))
unit= input("(L) bs or (K)g:")
if unit.upper() == "L":
   converted = weight * 0.45
   print(f'You are {converted} kilos')
else:
    converted= weight/0.45
    print(f"You are {converted} pounds")