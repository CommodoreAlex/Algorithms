# Stacks with recursion

# The factorial function
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1) # X has two different values here

print(fact(5)) # 5! = 5 * 4 * 3 * 2 * 1
print(fact(3)) # 3! = 3 * 2 * 1
