# basic calculator
# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

# cleaner version
# declares that x and y are integers right away
x = float(input("What's x? "))
y = float(input("What's y? "))

# adds x and y, then prints the result formatted with a thousands separator
# and two decimal places (keep cents). This uses the f-string format specifier
# `:,.2f` which adds commas and shows exactly two decimal digits.
z = x / y

print(f"{z:.2f}")