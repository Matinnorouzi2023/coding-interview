# Today's Goals (Arrays):
# Question 1: Rotate Array - Given an array, rotate the array to the right by k steps,
# where k is non-negative.
# TODO: Solution1
def rotate_array1(array, k):
    if len(array) == 0:
        return []
    k = k % len(array)
    temp = array[-k:]
    for i in reversed(range(0, (len(array)-k))):
        array[i+k] = array[i]
    for i in range(len(temp)):
        array[i] = temp[i]
    return array


print(rotate_array1([1, 2, 3, 4, 5], 3))

# TODO: Solution2


def reverse2(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
    start += 1
    end -= 1
    return array


def rotate_array2(array, k):
    k = k % len(array)
    reverse2(array, 0, len(array)-1)
    reverse2(array, 0, k - 1)
    reverse2(array, k, len(array)-1)
    return array


print(rotate_array2([1, 2, 3, 4, 5], 3))
