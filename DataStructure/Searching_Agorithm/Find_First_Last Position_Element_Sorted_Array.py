# TODO: Question 1:Find First and Last Position of Element in Sorted Array-
#  You are given an array of integers sorted in non-decreasing order,
#  find the starting and ending position of a given target value.
#  If target is not found in the array, return [-1, -1].
#  You must write an algorithm with O(log n) runtime complexity.

def find_left_extreme(array, target, range, left, right):
  if left > right:
    return

  middle = (left + right) // 2
  if array[middle] == target:
    if middle == 0:
      range[0] = 0
    elif array[middle - 1] == target:
      find_left_extreme(array, target, range, left, middle - 1)
    else:
      range[0] = middle
  elif target < array[middle]:
    find_left_extreme(array, target, range, left, middle - 1)
  else:
    find_left_extreme(array, target, range, middle + 1, right)


def find_right_extreme(array, target, range, left, right):
  if left > right:
    return

  middle = (left + right) // 2
  if array[middle] == target:
    if middle == len(array) - 1:
      range[1] = middle
    elif array[middle + 1] == target:
      find_right_extreme(array, target, range, middle + 1, right)
    else:
      range[1] = middle
  elif target < array[middle]:
    find_right_extreme(array, target, range, left, middle - 1)
  else:
    find_right_extreme(array, target, range, middle + 1, right)


def search_for_range(array, target):
  range = [-1, -1]
  find_left_extreme(array, target, range, 0, len(array) - 1)
  find_right_extreme(array, target, range, 0, len(array) - 1)
  return range


print(search_for_range([1, 1, 2, 2, 2, 3, 4], 2))

