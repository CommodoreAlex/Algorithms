# Selection Sort Algorithm: 

# Find the smallest element in the array
def findSmallest(arr):

    smallest = arr[0]  # Store the first element as the initial smallest value
    smallest_index = 0 # Store its index

    # Loop through remaining elements starting from index 1
    for i in range(1, len(arr)):
        if arr[i] < smallest:    # Compare each element with the current smallest value
            smallest = arr[i]    # Update smallest_value if a smaller element is found
            smallest_index = i   # Update smallest_index accordingly
    return smallest_index        # Return the index of the smallest element found

# Sorts an array
def selectionSort(arr):

    newArr = []           # Create an empty list to store sorted elements
    copiedArr = list(arr) # Original array is copied to avoid modifying input

    # Loop through all elements in copiedArr
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)      # Identify the smallest element index
        newArr.append(copiedArr.pop(smallest))  # Remove the smallest and add it to newArr
    return newArr                               # Return the fully sorted list

# Running the algorithm with an array as the parameter
print(selectionSort([5, 3, 6, 2, 10]))
