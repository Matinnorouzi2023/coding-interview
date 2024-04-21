# todo:Question 1:Invert Binary Tree- recursive way
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
# Code: Recursive
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


def invertRecursive(node):
  if node is None:  # Check if node is null (Time Complexity: O(1))
    return

  # Swap the nodes (Time Complexity: O(1))
  temp = node.left
  node.left = node.right
  node.right = temp

  # Perform the same operations for the left and right child nodes
  invertRecursive(node.left)  # Recursive call (Time Complexity: T(n/2))
  invertRecursive(node.right)  # Recursive call (Time Complexity: T(n/2))

  # Therefore, the overall Time Complexity of the function is O(n),
  # where n is the total number of nodes in the binary tree. This is because
  # each node in the tree is visited exactly once.
  return node


# Part
# 2 -


def invertRecursive(node):
  if node is None:  # Check if node is null (Space Complexity: O(1))
    return

  # Swap the nodes (Space Complexity: O(1))
  temp = node.left
  node.left = node.right
  node.right = temp

  # Perform the same operations for the left and right child nodes
  invertRecursive(node.left)  # Recursive call (Space Complexity: O(h/2))
  invertRecursive(node.right)  # Recursive call (Space Complexity: O(h/2))

  # The overall Space Complexity of the function is O(h), where h is
  # the height of the binary tree. This is because in a recursive function,
  # space is required to store the recursive call stack. The deepest
  # the recursion can go is till the height of the tree.
  return node


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
    if len(array) == 0:
      return
    i = 0
    if self.root is None:
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
      if current.left is None:
        if array[i] is not None:
          node = Node(array[i])
          current.left = node
        i += 1
        if i == len(array):
          return self
      if current.left is not None:
        queue.append(current.left)
      if current.right is None:
        if array[i] is not None:
          node = Node(array[i])
          current.right = node
        i += 1
        if i == len(array):
          return self
      if current.right is not None:
        queue.append(current.right)


def invertRecursive(node):
  if node is None:
    return

  temp = node.left
  node.left = node.right
  node.right = temp

  invertRecursive(node.left)
  invertRecursive(node.right)
  return node


tree = BinaryTree()
tree.insert([1, 2, 3, 4, None, None, 5, 6, None, 7])

invertRecursive(tree.root)