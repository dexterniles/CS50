# basic calculator
# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

# cleaner version
# declares that x and y are integers right away
x = float(input("What's x? "))
y = float(input("What's y? "))

# adds x and y, then rounds the result to the nearest integer before printing
print(round(x + y))