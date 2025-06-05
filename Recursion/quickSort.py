# QuickSort | Divide and Conquer (D&C) Algorithm (recursive)
# Figure out your base case, simplest possible case, or divide and decrease your problem until it becomes the base case.

def quicksort(array):
    if len(array) < 2:
        return array  # Base case for empty list or one element
    else:
        pivot = array[0] # Pivot point is first element
        less = [i for i in array[1:] if i <= pivot] # Sub array of all elements. Only keep elements less than or equal to pivot
        greater = [i for i in array[1:] if i > pivot] # Sub array of all elements. Only keep elements greater than pivot
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
