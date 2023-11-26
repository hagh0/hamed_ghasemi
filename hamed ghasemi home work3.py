def mergesort(numbers_list):
    if len(numbers_list) <= 1:
        return numbers_list

    mid = len(numbers_list) // 2
    left = mergesort(numbers_list[:mid])
    right= mergesort(numbers_list[mid:])

    return merge(left, right)

def merge(left, right):
    merged_numbers = []
    while left and right:
        if left[0] <= right[0]:
            merged_numbers.append(left.pop(0))
        else:
            merged_numbers.append(right.pop(0))

    merged_numbers += left or right

    return merged_numbers

numbers_list = [12,60,10,5,3,4,8,35,20]
sort_marge = mergesort(numbers_list)
print(sort_marge)