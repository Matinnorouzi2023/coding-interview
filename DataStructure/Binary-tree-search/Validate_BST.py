#TODO: Convert Sorted Array to Binary Search Tree
# You are given an array where the elements are strictly in increasing
# (ascending) order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which
# the depth of the two subtrees of every node does not differ by more than 1.

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, array):
    if len(array) == 0:
      return
    i = 0
    # if root is null
    if not self.root:
      if array[0] is None:
        return
      else:
        node = Node(array[0])
        self.root = node
        i += 1
        if i == len(array):
          return self
    # insert elements
    queue = [self.root]
    while queue:
      current = queue.pop(0)
      # left
      if not current.left:
        if array[i] is not None:
          node = Node(array[i])
          current.left = node
        i += 1
        if i == len(array):
          return self
      if current.left:
        queue.append(current.left)
      # right
      if not current.right:
        if array[i] is not None:
          node = Node(array[i])
          current.right = node
        i += 1
        if i == len(array):
          return self
      if current.right:
        queue.append(current.right)


# Function to check whether a tree is a valid BST
def check_if_valid_bst(root):
  return helper(root, float('-inf'), float('inf'))


# Helper function to recursively check BST property
def helper(node, min_val, max_val):
  # Base case
  if not node:
    return True

  value = node.value
  if value <= min_val or value >= max_val:
    return False

  # Node's left subtree and right subtree are valid BSTs
  is_left_bst = helper(node.left, min_val, value)
  is_right_bst = helper(node.right, value, max_val)

  return is_left_bst and is_right_bst


# Create a BinaryTree instance
tree = BinaryTree()
tree.insert([10, 5, 20, 3, 7, 15, 30, None, 4, None, None, None, 17, None, None, None, None, None, 18])

# Check if the tree is a valid BST
check_if_valid_bst(tree.root)

# Part
# 1: Code
# with Comments explaining Time Complexity
#
# Part
# 2: Code
# with Comments explaining Space Complexity
#
# Part
# 3: Full
# code
# including
# creating
# Binary
# tree
# for you to try out
#
# Part
# 1 -


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def checkIfValidBST(root):
  return helper(root, float('-inf'),
                float('inf'))  # Use Python's built-in representation for negative and positive infinity


def helper(node, min_val, max_val):
  # Base case
  if node is None:
    return True

  value = node.value
  # The current node's value must be between min_val and max_val
  if value <= min_val or value >= max_val:
    return False

  # Check if the left and right subtrees are valid BSTs
  # The left subtree's values must all be less than the current node's value
  # The right subtree's values must all be greater than the current node's value
  isLeftBST = helper(node.left, min_val, value)  # Time complexity is O(n/2)
  isRightBST = helper(node.right, value, max_val)  # Time complexity is O(n/2)

  return isLeftBST and isRightBST  # Combine two results


# Final time complexity is O(n), where n is the total number of nodes in the tree.
# This is because each node is visited once during the traversal.
# Part
# 2 -


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def checkIfValidBST(root):
  return helper(root, float('-inf'),
                float('inf'))  # Use Python's built-in representation for negative and positive infinity


def helper(node, min_val, max_val):
  # Base case
  if node is None:
    return True

  value = node.value
  # The current node's value must be between min_val and max_val
  if value <= min_val or value >= max_val:
    return False

  # Check if the left and right subtrees are valid BSTs
  # The left subtree's values must all be less than the current node's value
  # The right subtree's values must all be greater than the current node's value
  isLeftBST = helper(node.left, min_val, value)  # Space complexity is O(n/2) for the recursive call stack
  isRightBST = helper(node.right, value, max_val)  # Space complexity is O(n/2) for the recursive call stack

  return isLeftBST and isRightBST  # Combine two results


# Final space complexity is O(h), where h is the height of the tree.
# This is because the maximum amount of space is used when the recursion goes the deepest, which happens to be the height of the tree.
# Part
# 3 -


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, array):
    if not array: return
    i = 0
    if self.root is None:
      if array[0] is None:
        return
      else:
        node = Node(array[0])
        self.root = node
        i += 1
        if i == len(array): return self
    # insert elements
    queue = [self.root]
    while queue:
      current = queue.pop(0)
      # left
      if current.left is None:
        if array[i] is not None:
          node = Node(array[i])
          current.left = node
        i += 1
        if i == len(array): return self
      if current.left: queue.append(current.left)
      # right
      if current.right is None:
        if array[i] is not None:
          node = Node(array[i])
          current.right = node
        i += 1
        if i == len(array): return self
      if current.right: queue.append(current.right)


def checkIfValidBST(root):
  return helper(root, float('-inf'), float('inf'))


def helper(node, min_val, max_val):
  # Base case
  if node is None:
    return True
  value = node.value
  if value <= min_val or value >= max_val:
    return False
  # The left subtree's values must all be less than the current node's value
  # The right subtree's values must all be greater than the current node's value
  isLeftBST = helper(node.left, min_val, value)
  isRightBST = helper(node.right, value, max_val)
  return isLeftBST and isRightBST


tree = BinaryTree()
tree.insert([10, 5, 20, 3, 7, 15, 30, None, 4, None, None, None, 17, None, None, None, None, None, 18])

print(checkIfValidBST(tree.root))