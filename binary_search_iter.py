# Binary Search Grokking algos exercises but in Python 3.

def binary_search(arr, item):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid +1
        else:
            high = mid -1
    return None


test1 = [1,2,3,4,5,6,7,8,9,10,11]
print(binary_search(test1, 9))
print(binary_search(test1, 20))
    

