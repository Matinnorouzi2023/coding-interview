#todo:
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    node = Node(value)
    if not self.root:
      self.root = node
      return self

    tree = self.root
    while True:
      if value < tree.value:
        # move left
        if not tree.left:
          tree.left = node
          return self
        tree = tree.left
      else:
        # move right
        # value >= tree.value
        if not tree.right:
          tree.right = node
          return self
        tree = tree.right

  def find(self, value):
    if not self.root:
      return False
    tree = self.root
    while tree:
      if value < tree.value:
        tree = tree.left
      elif value > tree.value:
        tree = tree.right
      elif value == tree.value:
        return tree
    return False

  def remove(self, value, current=None, parent=None):
    if not self.root:
      return False
    if current is None:
      current = self.root
    while current:
      if value < current.value:
        parent = current
        current = current.left
      elif value > current.value:
        parent = current
        current = current.right
      else:
        # found the node to be deleted
        # node to be deleted has 2 children
        if current.left is not None and current.right is not None:
          current.value = self.get_min(current.right)
          self.remove(current.value, current.right, current)
        # if deleting the root node
