# Sum function exercise 4.1

def sum_list(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_list(list[1:])


test = [2,4,3,5,1]

print(sum_list(test))
