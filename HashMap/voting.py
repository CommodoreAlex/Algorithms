# Creating a dictionary
voted = {}

# Value is true if "tom" is in the hash table, otherwise evaluates to False
def check_voter(name):
    if name in voted:
        print("kick them out!")
    elif name == "mike":
        print("he cannot vote!")
    else:
        voted[name] = True
        print("let " + name + " vote!")

# Testing inputs
check_voter("tom")
check_voter("tyler")
check_voter("mike")
