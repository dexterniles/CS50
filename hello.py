# Ask user for their name, strip leading/trailing whitespace, and title-case it
# name = input("What's your name? ").strip().title()

# Split user's name into parts
# first, last = name.split(" ")

# Say hello to user
# end="" prevents automatic newline after print
# sep="" prevents spaces between printed items
# print(f"Hello, {name}!") will format the string with the user's name
# print("Hello, " + first + "!")

# def hello(to="world"):
#    print("Hello,", to)

# hello()
# name = input("What's your name? ")
# hello(name)

def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()