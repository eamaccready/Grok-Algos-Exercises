# Exercise 4.4 binary search recurse.

def bin_search_recurse(arr, low, high, num):
    if low > high:
        return -1
    mid = (low + high)// 2
    guess = arr[mid]
    if guess == num:
        return mid
    if guess < num:
        return bin_search_recurse(arr, mid+1, high, num)
    else:
        return bin_searc_recurse(arr, low, mid-1, num)

test= [1,2,3,4,5,6,7,8,9,10,11]

print(bin_search_recurse(test, 0, len(test)-1, 9))
print(bin_search_recurse(test, 0, len(test)-1, 16))
                                
