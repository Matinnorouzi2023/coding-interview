#todo: Convert Sorted Array to Binary Search Tree
# You are given an array where the elements are strictly in increasing
# (ascending) order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of
# the two subtrees of every node does not differ by more than 1.

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def build_bst_from_sorted_array(nums, left=0, right=None):
  if right is None:
    right = len(nums) - 1

  # Base case
  if left > right:
    return None

  middle = (left + right) // 2
  node = Node(nums[middle])
  node.left = build_bst_from_sorted_array(nums, left, middle - 1)
  node.right = build_bst_from_sorted_array(nums, middle + 1, right)

  return node


# Example usage
build_bst_from_sorted_array([1, 2, 3, 4, 5])

# Python
# code
# Part
# 1: Code
# with Comments explaining Time Complexity
#
# Part
# 2: Code
# with Comments explaining Space Complexity
#
# Part
# 1 -


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def buildBSTfromSortedArray(nums, left=0, right=None):
  if right is None:
    right = len(nums) - 1

  # Base case
  if left > right:
    return None

  # The middle element of the array becomes the root of the tree
  middle = (left + right) // 2  # Time complexity of this operation is O(1)
  node = Node(nums[middle])  # Time complexity of this operation is O(1)

  # Recursively build the left and right subtrees
  # As this operation is performed recursively on each half of the array,
  # its time complexity is O(n), where n is the number of elements in the array
  node.left = buildBSTfromSortedArray(nums, left, middle - 1)
  node.right = buildBSTfromSortedArray(nums, middle + 1, right)

  # At this point, the tree has been constructed
  return node


# Final time complexity: O(n)
# Part
# 2 -


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def buildBSTfromSortedArray(nums, left=0, right=None):
  if right is None:
    right = len(nums) - 1

  # Base case
  if left > right:
    return None

  middle = (left + right) // 2
  node = Node(nums[middle])  # Space complexity of this operation is O(1)

  # Recursively build the left and right subtrees
  # As this operation is performed recursively on each half of the array,
  # its space complexity is O(log(n)), where n is the number of elements in the array
  # This is due to the space required by the call stack for the recursive calls
  node.left = buildBSTfromSortedArray(nums, left, middle - 1)
  node.right = buildBSTfromSortedArray(nums, middle + 1, right)

  # At this point, the tree has been constructed
  return node

# Final space complexity: O(log(n)+ n) = O(n) ( as the BST has n elements)