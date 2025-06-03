# Binary Search Algorithm

def binary_search(arr, target):

    # Initialize left and right (low and high)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Check the middle element
        guess = arr[mid]

        if guess == target:      # Guess was correct
            return mid
        elif guess > target: 
            high = mid - 1       # The guess was too high
        else:
            low = mid + 1        # The guess was too low

# Array to check against
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # Lists start at zero, the second slot has index 1
print(binary_search(my_list, -1)) # None (null in Python)
