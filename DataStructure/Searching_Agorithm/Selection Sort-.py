#todo :
# Question 1:Selection Sort-
# You are given an array of integers.
# Write a function that will take this array as input and return
# the sorted array using Selection sort.

def selection_sort(array):
  for i in range(len(array)):
    smallest = i
    for j in range(i + 1, len(array)):
      if array[j] < array[smallest]:
        smallest = j
    if i != smallest:
      # swap i and smallest
      array[i], array[smallest] = array[smallest], array[i]
  return array
#todo :
# T= o(n^2) = n-1 + n-2+ ... 1
# s=o(1)

print(selection_sort([4, 3, 2, 1]))


