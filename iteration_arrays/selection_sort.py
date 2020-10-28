def find_smallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)-1):
        current = list[i]
        #print("i is {}, current is {}.".format(i,current))
        if current < smallest:
            smallest = current
            smallest_index = i
    return smallest_index

def selection_sort(list):
    result = []
    for j in range(len(list)):
        item = find_smallest(list)
        print("item is: {}".format(item))
        temp = list.pop(item)
        print("temp is {}".format(temp))
        result.append(temp)
        #result.append(list.pop(item))
    return result

test = [5,3,6,2,10]

print(selection_sort(test))
