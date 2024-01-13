# TODO: Question 1:Binary Search -
#  Given an array of integers which is sorted in ascending order,
#  and a target integer, write a function to search
#  for whether the target integer is there in the given array.
#  If it is there then return its index. Otherwise, return -1.
#  You must write an algorithm with O(log n) runtime complexity.

#TODO: METHOD1 : ITERATIVE
# TIME= O(LOG N)
# SPACE = O(1)--->- Didn't use any auxulary store
def binary_search_iterative(array,target):
  left = 0
  right = len(array)-1
  while left <=  right:
    middle = (left+right)//2
    if array[middle] == target:
      return middle
    elif array[middle] < target:
      left = middle+1
    else:
      right = middle - 1
  return -1


print(binary_search_iterative([2, 3, 7, 9, 11, 23, 37, 81, 87, 89 ],87))

#TODO: METHOD2 : RECURSIVE
# TIME= O(LOG N)
# SPACE = O(LOG N)

def binary_search_recursive(nums, target):
  def helper(nums, target, left, right):
    if left > right : return -1
    middle =(left+right)//2
    if nums[middle] == target :
      return middle
    elif nums[middle]<target:
      return helper(nums, target, middle+1, right)
    else:
      return helper(nums, target, left, middle-1)
  return helper(nums,target,0,len(nums)-1)

print(binary_search_recursive([2, 3, 7, 9, 11, 23, 37, 81, 87, 89 ],9))