# Max in list.

def list_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        curr_max = max(list[1:])
        return list[0] if list[0] > curr_max else curr_max

test = [1,4,3,9,2,5,7]
print(list_max(test))
