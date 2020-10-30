import math

print("Please enter the number of coins: ")
print("# of quarters: ")
quarters = int(input())
print("# of dimes: ")
dimes = int(input())
print("# of nickels: ")
nickels = int(input())
print("# of pennies: ")
pennies = int(input())

total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01

dollars = int(total)
cents = int(total % int(total) * 100)

print(f"The total is {dollars} dollars and {cents} cents")