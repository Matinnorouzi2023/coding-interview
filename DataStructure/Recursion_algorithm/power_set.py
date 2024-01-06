# TODO : Power Set - Given an integer array of unique elements,
#  return all possible subsets (the power set).
#  The solution set must not contain duplicate subsets.
#  Return the solution in any order.
#
# All the best!
class Solution(object):

  def power_set(self, nums):
      output = []
      def backtrack(nums, i, subset):
        if i == len(nums):
          output.append(subset.copy())
          return
        backtrack(nums, i + 1, subset)
        subset.append(nums[i])
        backtrack(nums, i + 1, subset)
        subset.pop()
      backtrack(nums, 0, [])
      return output


sol = Solution()
print(sol.power_set([1, 8, 7]))

T= O(2^*N/2)=O(2^*N)
S= O(2^*N/2)=O(2^*N)