#todo:
# time=space=(1)= no need to travers
# todo:2Question 2:
#  DLL remove all, insert at position Create a Doubly Linked List class.
#  Write Instance Methods for this class to be able to
#  1. remove all the nodes in the doubly linked list which have their value
#  equal to a given value.
#  2.Insert a node at a desired position (node and position are given).
#  The Linked List is 0 indexed. If given node is a node existing
#  in the Linked List shift it to the desired position.
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

  def insertB(self, nodePosition, nodeInsert):
    if self.head == nodeInsert and self.tail == nodeInsert:
      return
    self.remove(nodeInsert)
    nodeInsert.prev = nodePosition.prev
    nodeInsert.next = nodePosition
    if nodePosition == self.head:
      self.head = nodeInsert
    else:
      nodePosition.prev.next = nodeInsert
    nodePosition.prev = nodeInsert
  def print_list(self):
    current = self.head
    while current:
      print(current.val, end=" ")
      current = current.next
    print()

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
seven = Node(7)
linkNodes(one, two)
linkNodes(two, three)
linkNodes(three, four)
linkNodes(four, five)
linkedListDoubly = DoublyLinkedList()
linkedListDoubly.head = one
linkedListDoubly.tail = five


# linkedListDoubly.remove(five)
# linkedListDoubly.insertB(two, three)
linkedListDoubly.insertB(three, seven)

linkedListDoubly.print_list()