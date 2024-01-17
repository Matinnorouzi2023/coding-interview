#todo: question 1:DLL remove insert
# Create a Doubly Linked List class.
# Write Instance Methods for this class to be able to
# 1.remove a node when the node to be removed is given as Input.
# 2. insert a node before a particular node(both the node to be inserted
# and the node before which the insertion is to happen will be given as input).
# If the node to be inserted is part of the linked list then
# shift its place to the desired location
# -a new node, then insert the new node at the place desired.

# #






class Node:
  def __init__(self, value):
    self.val = value
    self.next = None
    self.prev = None


def linkNodes(node1, node2):
  node1.next = node2
  node2.prev = node1


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def remove(self, node):
    if self.head == node:
      self.head = node.next
    if self.tail == node:
      self.tail = node.prev
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    node.next = None
    node.prev = None

  def print_list(self):
    current = self.head
    while current:
      print(current.val, end=" ")
      current = current.next
    print()


# null - 1 - 2 - 3 - 4 - 5 - null
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
linkedListDoubly = DoublyLinkedList()
linkNodes(one, two)
linkNodes(two, three)
linkNodes(three, four)
linkNodes(four, five)
linkedListDoubly.head = one
linkedListDoubly.tail = five


linkedListDoubly.remove(five)

linkedListDoubly.print_list()
