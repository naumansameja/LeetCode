


# def modified_binary_search(array, elt, start, end):
# mid = (start+end)//2
#     if array[mid] == elt:
#         return mid
#     if start > end:
#         return -1
#     
    
#     if array[start] < array[end]:
#         if array[mid] < elt:
#             return modified_binary_search(array, elt, mid+1, end)
#         return modified_binary_search(array, elt, start, mid-1)
#     if array[start] <= elt and array[end] < elt:
#         return modified_binary_search(array, elt, start, mid-1)
#     return modified_binary_search(array, elt, mid+1, end)
array = [8,1,2,3]

array2 = [9,0,1,2,3, 4,5,6,7,8]
array3 = [4,5,6,7,0,1,2]


def modified_binary_search(array, elt, start, end):
    mid = (start+end)//2
    if array[mid] == elt:
        return mid
    if start >= end:
        return -1
    
    
    if array[mid+1] > array[end]:
        if array[start] <= elt and array[mid] >= elt:
            return modified_binary_search(array, elt, start, mid-1)
        return modified_binary_search(array, elt, mid+1, end)
    
    if array[start] >= array[mid]:
        if array[mid+1] <= elt and array[end] >= elt:
            return modified_binary_search(array, elt, mid+1, end)   
        return modified_binary_search(array, elt, start, mid-1)
    if array[mid+1] <= elt and array[end] >=  elt:
        return modified_binary_search(array, elt, mid+1, end)  
    return modified_binary_search(array, elt, start, mid-1)


    

print(modified_binary_search(array, 1,0, len(array) -1))
print(modified_binary_search(array2, 1,0, len(array2) -1))
print(modified_binary_search(array3, 1,0, len(array3) -1))