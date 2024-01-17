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
        elif parent is None:
          if current.left is not None:
            current.value = current.left.value
            current.left = current.left.left
            current.right = current.left.right
          elif current.right is not None:
            current.value = current.right.value
            current.left = current.right.left
            current.right = current.right.right
          else:
            # this is a single node bst
            self.root = None
        elif current == parent.left:
          parent.left = current.left if current.left is not None else current.right
        elif current == parent.right:
          parent.right = current.left if current.left is not None else current.right
        # break out of the while loop
        break
    return self

  def get_min(self, node):
    while node.left is not None:
      node = node.left
    return node.value


# Create Binary Search Tree
bst = BinarySearchTree()
bst.insert(20)
bst.insert(6)
bst.insert(35)
bst.insert(3)
bst.insert(8)
bst.insert(27)
bst.insert(55)
bst.insert(1)
bst.insert(3)
bst.insert(25)
bst.insert(29)
bst.insert(60)
