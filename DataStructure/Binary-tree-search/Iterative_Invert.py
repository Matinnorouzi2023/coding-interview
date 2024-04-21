# todo:Question 1:Invert Binary Tree-iterative way
#  Given the root of a binary tree, invert the tree, and return its root.
#  (Invert means swap every left node for
#  its corresponding right node / get mirror image)


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


def invert_iterative(root):
  if not root:
    return None
  queue = [root]
  while queue:
    current = queue.pop(0)
    temp = current.right
    current.right = current.left
    current.left = temp
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return root


# Create a BinaryTree instance
tree = BinaryTree()

# Insert elements into the tree
tree.insert([1, 2, 3, 4, None, None, 5, 6, None, 7])

# Invert the tree iteratively
invert_iterative(tree.root)

# Python
# Code: Iterative
# Note: In
# Python, a
# deque
# stands
# for a "double-ended queue".It's part of the collections module and provides an efficient way to handle operations at both ends of a collection. This includes operations like appending and popping elements.
#
# Alternatively
# you
# can
# implement
# the
# queue
# with a LL as well.In an interview you can also go ahead and implement it with an array after mentioning to the interviewer that you are doing this just to save time
#
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
# along
# with code to create the binary tree ( for you to
# try out )
#
# Part 1 -

from collections import deque


def invertIterative(root):
  if root is None:
    return  # No operation required if root is None, hence O(1) time complexity.

  queue = deque([root])  # We use a queue for bfs of the tree.

  while queue:  # This loop runs once for each node in the tree, hence O(n) time complexity, where n is the number of nodes.
    current = queue.popleft()  # This operation takes O(1) time in Python deque.
    current.left, current.right = current.right, current.left  # Swapping takes O(1) time.
    if current.left:
      queue.append(current.left)  # This operation takes O(1) time.
    if current.right:
      queue.append(current.right)  # This operation takes O(1) time.

  return root  # This operation takes O(1) time.


# Final time complexity: O(n), where n is the number of nodes in the tree.
# Part
# 2 -

from collections import deque


def invertIterative(root):
  if root is None:
    return  # No additional space is used, hence O(1) space complexity.

  queue = deque([root])  # We use a queue for bfs of the tree. In worst case scenario, the maximum size
  # of the queue is the width of the tree, which could be equal to the number of nodes in the tree.
  # Hence, the space complexity is O(n), where n is the number of nodes in the tree.

  while queue:
    current = queue.popleft()
    current.left, current.right = current.right, current.left
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return root


# Final space complexity: O(n), where n is the number of nodes in the tree.
# Part
# 3 -

from collections import deque


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
    if self.root is None:
      if array[0] is None:
        return
      else:
        node = Node(array[0])
        self.root = node
        i += 1
        if i == len(array):
          return self
    # insert elements
    queue = deque([self.root])
    while queue:
      current = queue.popleft()
      # left
      if current.left is None:
        if array[i] is not None:
          node = Node(array[i])
          current.left = node
        i += 1
        if i == len(array):
          return self
      if current.left is not None:
        queue.append(current.left)
      # right
      if current.right is None:
        if array[i] is not None:
          node = Node(array[i])
          current.right = node
        i += 1
        if i == len(array):
          return self
      if current.right is not None:
        queue.append(current.right)


def invertIterative(root):
  if root is None:
    return
  queue = deque([root])
  while queue:
    current = queue.popleft()
    temp = current.right
    current.right = current.left
    current.left = temp
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return root


tree = BinaryTree()
tree.insert([1, 2, 3, 4, None, None, 5, 6, None, 7])

invertIterative(tree.root)