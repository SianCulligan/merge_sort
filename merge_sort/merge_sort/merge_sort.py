testing_list = [8,4,16,23,15]
test_with_negative = [8,4,-16,23,15]

def merge_sort(og_list):
    list_length = len(og_list)
    mid = round(list_length/2)
    left = []
    right = []
    
    if(list_length < 2):
        return "Need more than 1 more number to sort"

    current = 0

    while current < mid:
        bool_err = type(og_list[current]) is int
        if bool_err is True:
            left.append(og_list[current])
            current += 1
        else:
            print("Error")
            return "Error"  
    while current < len(og_list):
        bool_err = type(og_list[current]) is int
        if bool_err is True:
            right.append(og_list[current])
            current += 1        
        else:
            print("Error")
            return "Error"  
    merge_sort(left)
    merge_sort(right)
    # print("LEFT", left)
    # print("right", right)
    merge(left, right, og_list)

def merge(left, right, og_list):
    i = 0
    j = 0
    k = 0
    # print("RIGT len", len(right))
    # print("LEFT len", len(left))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            og_list[k] = left[i]
            i += 1
        else:
            og_list[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        og_list[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        og_list[k] = right[j]
        j += 1
        k += 1
    
    print("OG LIST", og_list)
    return og_list



# merge_sort(testing_list)