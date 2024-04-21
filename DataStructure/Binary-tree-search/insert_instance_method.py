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
    if not self.root:
      if array[0] is None:
        return
      else:
        node = Node(array[0])
        self.root = node
        i += 1
        if i == len(array):
          return self
    queue = [self.root]
    while queue:
      current = queue.pop(0)
      if not current.left:
        if array[i] is not None:
          node = Node(array[i])
          current.left = node
        i += 1
        if i == len(array):
          return self
      if current.left:
        queue.append(current.left)
      if not current.right:
        if array[i] is not None:
          node = Node(array[i])
          current.right = node
        i += 1
        if i == len(array):
          return self
      if current.right:
        queue.append(current.right)

  def printinsert(self, current=None):
    if current is None:
      current = self.root

    if current:
      if current.left:
        self.printinsert(current.left)
      print(current.value)
      if current.right:
        self.printinsert(current.right)


# Create a BinaryTree instance
tree = BinaryTree()

# Insert elements into the tree
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])

# Print the elements of the tree
tree.printinsert()

# Python - Insert: inserts
# elements
# from an array
#
# into
# a
# binary
# tree
# level
# by
# level.
#

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

    # If root is null
    if self.root is None:
      if array[0] is None:
        return
      else:
        node = Node(array[0])
        self.root = node
        i += 1
        if i == len(array):
          return self

    # Insert elements
    queue = [self.root]
    while queue:
      current = queue.pop(0)

      # Process left child
      if current.left is None:
        if array[i] is not None:
          node = Node(array[i])
          current.left = node
        i += 1
        if i == len(array):
          return self
      if current.left is not None:
        queue.append(current.left)

      # Process right child
      if current.right is None:
        if array[i] is not None:
          node = Node(array[i])
          current.right = node
        i += 1
        if i == len(array):
          return self
      if current.right is not None:
        queue.append(current.right)


# Create a binary tree and insert elements
tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])

