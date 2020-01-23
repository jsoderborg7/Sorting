# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
# both passed arrays start at 0 index
    a_index = 0
    b_index = 0
# loop through the length 
    for i in range(0, elements):
# check for smallest element in both arrays and assign to merged_arr
        if a_index >= len(arrA):
          merged_arr[i] = arrB[b_index]
          b_index += 1
        elif b_index >= len(arrB):
          merged_arr[i] = arrA[a_index]
          a_index += 1
        elif arrA[a_index] < arrB[b_index]:
          merged_arr[i] = arrA[a_index]
          a_index += 1
        else:
          merged_arr[i] = arrB[b_index]
          b_index += 1  
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # get the middle of the array
    if len(arr) > 1:
      mid = len(arr)//2
      # then split into left and right sides
      leftside = arr[:mid]
      rightside = arr[mid:]
      # now the fun recursion part
      left = merge_sort(leftside)
      right = merge_sort(rightside)
      arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
