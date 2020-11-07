# Quicksort. Non ideal pivot. Grokk Algo Code.
# Would be O(n^2) on a sorted list.
# Updated code to concat list correctly.

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# My Test.
test = [10, 5, 2, 3, 6, 4]

print(quicksort(test))
