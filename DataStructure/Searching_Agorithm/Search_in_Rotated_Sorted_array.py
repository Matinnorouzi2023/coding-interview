# TODO :
#  Question 2:Search in Rotated Sorted array:
#  You are given an integer array nums sorted in ascending order (with distinct values).
#  Prior to being passed to your function, nums is possibly rotated at
#  an unknown pivot index k (1 <= k < nums.length) such that the resulting array
#  is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
#  For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#  Given an integer target, return the index of target if it is in the array, else return -1.
#  You must write an algorithm with O(log n) runtime complexity.
def search_rotated_sorted_array(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = (left+right)//2
        if nums[middle] == target: return middle
        if nums[left] <= nums[middle]:
           #left part is sorted
          if target >= nums[left] and target< nums[middle]:
               #explore left part
                right = middle - 1
          else:
                left = middle +1
        else:
          #right part is sorted
          if target<= nums[right] and target > nums[middle]:
               left = middle +1
          else:
               right = middle -1
    return  -1

print(search_rotated_sorted_array([7,8,1,2,3,4,5,6,],3))

#todo : time complexity = o(logn)
#todo: space complexity s= o(1) -------> for iteration and s=(n) -----> recursive

# class Solution:
#   def search(self, nums: search[int], target: int) -> int:
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#       middle = (left + right) // 2
#       if nums[middle] == target:
#         return middle
#
#       if nums[left] <= nums[middle]:
#         # Left part is sorted
#         if target >= nums[left] and target < nums[middle]:
#           # Explore left part
#           right = middle - 1
#         else:
#           left = middle + 1
#       else:
#         # Right part is sorted
#         if target <= nums[right] and target > nums[middle]:
#           left = middle + 1
#         else:
#           right = middle - 1
#
#     return -1
#
#
# sol = Solution()
# print(sol.search([7, 8, 1, 2, 3, 4, 5, 6], 3))

