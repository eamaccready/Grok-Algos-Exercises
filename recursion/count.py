# Count Arr recurse exercise 4.2

def count(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + count(list[1:])


test = [1,2,3,4,5]
        
print(count(test))
