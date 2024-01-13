#todo :
# Question 2:Merge Sort-
# You are given an array of integers.
# Write a function that will take this array as input and return
# the sorted array using Merge sort.

#todo:
# time = o(m+n)
# space = o(m+n)

def mergeSortedArrays(array1, array2):
  mergedArray = []
  i = j = 0
 
  while i < len(array1) and j < len(array2):
    if array1[i] <= array2[j]:
      mergedArray.append(array1[i])
      i += 1
    else:
      mergedArray.append(array2[j])
      j += 1

  while i < len(array1):
    mergedArray.append(array1[i])
    i += 1

  while j < len(array2):
    mergedArray.append(array2[j])
    j += 1

  return mergedArray


class Math:

  def mergeSort(array):
    if len(array) <= 1:
      return array
    middle = len(array) // 2
    leftside = Math.mergeSort(array[:middle])
    rightside = Math.mergeSort(array[middle:])
    return mergeSortedArrays(leftside, rightside)


# Example usage:
array = [5, 3, 7, 8, 1, 9, 12]
sorted_array = Math.mergeSort(array)
print(sorted_array)