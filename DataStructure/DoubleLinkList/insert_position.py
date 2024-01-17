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

  def allNodesValueRemove(self, value):
    curr = self.head
    while curr:
      temp = curr
      curr = curr.next
      if temp.val == value:
        self.remove(temp)

  def insertPosition(self, position, node):
    curr = self.head
    counter = 0
    while curr is not None and counter != position:
      curr = curr.next
      counter += 1
    if curr is not None:
      self.insertB(curr, node)
    else:
      if self.head is None:
        self.head = node
        self.head = node
      else:
        self.remove(node)
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

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
linkedListDoubly = DoublyLinkedList()
linkNodes(one, two)
linkNodes(two, three)
linkNodes(three, four)
linkNodes(four, five)
linkedListDoubly.head = one
linkedListDoubly.tail = five
linkedListDoubly.insertPosition(20, four)


linkedListDoubly.print_list()
#todo:insert in shift position----> best-time= o(1), worst_time=o(n) space=o(n)