# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # 0(n)
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # i is indices of left and j is indices of right
    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            # value on the left list is smaller (or equal so it should be selected)
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1

        k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    # while i < len(arrA):
    #     merged_arr[k] = arrA[i]
    #     i += 1
    #     k += 1

    # while j < len(arrB):
    #     merged_arr[k] = arrB[j]
    #     j += 1
    #     k += 1

    # shortcut if done with left can copy rest of other list up to merged array

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:  # base case, stop cutting in half here
        return arr

    # cutting in half until base case (each list has 1 (sorted) item)
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursion to divide subarrays until each has 1 element
    left = merge_sort(left)
    right = merge_sort(right)

    # each subarray has 1 (sorted) item, so compare and merge
    arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return

    # pointers to maintain start of both arrays
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = (l + r) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)

        merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
