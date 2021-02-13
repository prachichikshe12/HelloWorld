# Conditional Statements

is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink a plenty of Water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm cloths")
else:
    print("Have a lovely Day")

print("Enjoy your day")


#Exercise:

price= 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: $ {down_payment}')

