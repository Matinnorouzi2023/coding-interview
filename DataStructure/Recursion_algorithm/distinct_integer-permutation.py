def permutations(nums):
    permutations =[]
    if len(nums)==0: return [[]]

    def helper(num,i):
      if i == len(num)-1:  #num =2
        permutations.append(nums.copy())
        return
      for j in range(i, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        helper(nums, i+1)
        nums[i], nums[j] = nums[j], nums[i]
    helper(nums,0)
    return permutations


print(permutations([1, 2, 3]))


class Solution(object):
  def permute(self, nums):
    def backtrack(start):
      if start == len(nums):
        result.append(nums[:])  # Append a copy of the current permutation
        return

      for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        backtrack(start + 1)
        nums[start], nums[i] = nums[i], nums[start]  # Backtrack

    result = []
    backtrack(0)
    return result


# Test the optimized code
sol = Solution()
print(sol.permute([1, 2, 3]))