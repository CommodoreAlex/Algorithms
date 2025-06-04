# Recursion Algorithm

# Improper implementation of recursion
def oldcountdown(i):
    print(i)
    oldcountdown(i-1)

# Properly implementing recursion
def countdownTwo(i):

    print(i)

    if i <= 1: # Base case
        return
    else: # Recursive case
        countdownTwo(i-1)

countdownTwo(10)
