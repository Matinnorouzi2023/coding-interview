# Todo:
#  Question 2:Left/Right View of binary tree
#  #
#  1. Given the root of a binary tree, imagine yourself standing on the right side
#  of it, return the values of the nodes you can see ordered from top to bottom.
#  2. Given the root of a binary tree, imagine yourself standing on the left side
#  of it, return the values of the nodes you can see ordered from top to bottom.

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


def right_view(root):
  if not root:
    return []
  right = []
  queue = [root]
  while queue:
    length = len(queue)
    count = 0
    while count < length:
      count += 1
      current = queue.pop(0)
      if count == length:
        right.append(current.value)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
  return right


def left_view(root):
  if not root:
    return []
  left = []
  queue = [root]
  while queue:
    length = len(queue)
    count = 0
    while count < length:
      count += 1
      current = queue.pop(0)
      if count == 1:
        left.append(current.value)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
  return left


# Create a BinaryTree instance
tree = BinaryTree()

# Insert elements into the tree
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])

# Call left_view or right_view as needed
# right_view(tree.root)
left_view(tree.root)

# Python
# code
# Part
# 1: Code
# with Insert function as well
#
# Part
# 2: Only
# Right
# view
# code
# with Time and Space complexity analysed
#
# Part
# 3: Only
# Left
# view
# code
# with Time and Space complexity analysed
#
# Part
# 1 -


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
    # if root is None
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
    queue = [self.root]
    while queue:
      current = queue.pop(0)
      # left
      if current.left is None:
        if array[i] is not None:
          node = Node(array[i])
          current.left = node
        i += 1
        if i == len(array):
          return self
      if current.left:
        queue.append(current.left)
      # right
      if current.right is None:
        if array[i] is not None:
          node = Node(array[i])
          current.right = node
        i += 1
        if i == len(array):
          return self
      if current.right:
        queue.append(current.right)


def rightView(root):
  if root is None:
    return []
  right = []
  queue = [root]
  while queue:
    length = len(queue)
    count = 0
    while count < length:
      count += 1
      current = queue.pop(0)
      if count == length:
        right.append(current.value)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
  return right


def leftView(root):
  if root is None:
    return []
  left = []
  queue = [root]
  while queue:
    length = len(queue)
    count = 0
    while count < length:
      count += 1
      current = queue.pop(0)
      if count == 1:
        left.append(current.value)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
  return left


tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])
print(leftView(tree.root))
# Part
# 2 -


def rightView(root):
  if root is None:
    return []  # No operation required if root is None, hence O(1) time and O(1) space complexity.

  right = []  # We will store the right view in this list. The size of the list is equal to the height of the tree.
  # Hence, the space complexity is O(h), where h is the height of the tree.

  queue = [root]  # We use a queue for level-order traversal of the tree. In worst case scenario, the maximum size
  # of the queue is the width of the tree, which could be equal to the number of nodes in the tree.
  # Hence, the space complexity is O(n), where n is the number of nodes in the tree.

  while queue:  # This loop runs once for each node in the tree, hence O(n) time complexity, where n is the number of nodes.

    length = len(queue)  # This takes O(1) time and space.
    count = 0  # This takes O(1) time and space.

    while count < length:  # This loop runs once for each node in the current level.
      # The total time complexity for this nested loop is still O(n), where n is the number of nodes.

      count += 1  # This takes O(1) time and space.

      current = queue.pop(
        0)  # This operation can take O(n) time complexity in worst case scenario as all the elements have to be shifted.

      if count == length:  # This takes O(1) time and space.
        right.append(current.value)  # This takes O(1) time and space.

      if current.left:
        queue.append(current.left)  # This takes O(1) time and space.

      if current.right:
        queue.append(current.right)  # This takes O(1) time and space.

  return right  # This takes O(1) time and space.


# Final time complexity: O(n) + O(n) = O(n), where n is the number of nodes in the tree.
# Final space complexity: O(n) + O(h) = O(n), where n is the number of nodes and h is the height of the tree.
# Part
# 3 -


def leftView(root):
  if root is None:
    return []  # No operation required if root is None, hence O(1) time and O(1) space complexity.

  left = []  # We will store the left view in this list. The size of the list is equal to the height of the tree.
  # Hence, the space complexity is O(h), where h is the height of the tree.

  queue = [root]  # We use a queue for level-order traversal of the tree. In worst case scenario, the maximum size
  # of the queue is the width of the tree, which could be equal to the number of nodes in the tree.
  # Hence, the space complexity is O(n), where n is the number of nodes in the tree.

  while queue:  # This loop runs once for each node in the tree, hence O(n) time complexity, where n is the number of nodes.

    length = len(queue)  # This takes O(1) time and space.
    count = 0  # This takes O(1) time and space.

    while count < length:  # This loop runs once for each node in the current level.
      # The total time complexity for this nested loop is still O(n), where n is the number of nodes.

      count += 1  # This takes O(1) time and space.

      current = queue.pop(
        0)  # This operation can take O(n) time complexity in worst case scenario as all the elements have to be shifted.

      if count == 1:  # This takes O(1) time and space.
        left.append(current.value)  # This takes O(1) time and space.

      if current.left:
        queue.append(current.left)  # This takes O(1) time and space.

      if current.right:
        queue.append(current.right)  # This takes O(1) time and space.

  return left  # This takes O(1) time and space.

# Final time complexity: O(n) + O(n) = O(n), where n is the number of nodes in the tree.
# Final space complexity: O(n) + O(h) = O(n), where n is the number of nodes and h is the height of the tree.