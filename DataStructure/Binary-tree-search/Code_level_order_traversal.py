#Todo :(Binary Trees):
# Question 1:Level Order traversal
# Write a function that takes the root of a binary tree,
# and returns the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).
# Initially write an instance method for the Binary Search tree class
# to insert the values given as an array into the Binary tree
# (from left to right, level by level).
# Each value in the array which is not null is to be made a node and
# added to the tree. (See examples below).
# Then write the function mentioned first.
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


def level_order_traversal(root):
  if not root:
    return []
  output = []
  queue = [root]
  while queue:
    length = len(queue)
    count = 0
    curr_level_values = []
    while count < length:
      curr = queue.pop(0)
      curr_level_values.append(curr.value)
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
      count += 1
    output.append(curr_level_values)
  return output


tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])
print(level_order_traversal(tree.root))

# Python code - Level order traversal
# Part 1: Code
# with Comments explaining Time Complexity
#
# Part2: Code
# with Comments explaining Space Complexity
#
# Part 1 -from collections import deque


def level_order_traversal(root):
  if root is None:  # This operation is O(1)
    return []

  output = []
  queue = deque([root])  # Creating a queue is O(1)
  while queue:  # The outer while loop will run for n iterations (n is the total number of nodes in the tree)
    length = len(queue)  # Getting the length of the queue is O(1)
    count = 0
    curr_level_values = []
    while count < length:  # This inner while loop will run for 'length' iterations
      curr = queue.popleft()  # Removing an element from the deque is O(1)
      curr_level_values.append(curr.value)  # Appending an element is O(1)
      if curr.left:
        queue.append(curr.left)  # Appending an element to deque is O(1)
      if curr.right:
        queue.append(curr.right)  # Appending an element to deque is O(1)
      count += 1
    output.append(curr_level_values)  # Appending a list of length 'length' is O(length)

  return output


''' Time Complexity: Since each node is processed exactly once and each operation inside 
the loops are either O(1) or O(length), the overall time complexity of the function is O(n) 
where n is the total number of nodes in the tree.'''
# Part 2 -

from collections import deque


def level_order_traversal(root):
  if root is None:
    return []

  output = []  # This list will hold the final output and will need space of O(n)
  queue = deque([
                  root])  # This queue will hold the nodes to be processed and in the worst case scenario (when the tree is a complete tree) it will need space of O(n/2) = O(n)
  while queue:
    length = len(queue)
    count = 0
    curr_level_values = []  # This list will hold the nodes at the current level and will need space of O(n)
    while count < length:
      curr = queue.popleft()
      curr_level_values.append(curr.value)
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
      count += 1
    output.append(curr_level_values)

  return output


'''Space Complexity: As we are storing the nodes in the queue and in the output list and 
also we are using some extra space for variables, the overall space complexity of the 
function is O(n) where n is the total number of nodes in the tree.'''