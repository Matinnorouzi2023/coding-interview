# todo: (Singly Linked List):-Linked List Data Structure Crash Course
#  Question 1:
#  Construct Singly Linked List -
#  Design a Singly linked list class that has a head and tail.
#  Every node is to have two attributes:
#  value:  the value of the current node, and
#  next: a pointer to the next node. The linked list is to be 0-indexed.
#  The class should support the following:
#  SinglyLinkedList() Initializes the SinglyLinkedList object.
#


# todo: Construct Singly Linked List -
#  Design a Singly linked list class that has a head and tail.


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# todo :Every node is to have two attributes:
#  value:  the value of the current node, and
#  next: a pointer to the next node. The linked list is to be 0-indexed.
#  #
#  The class should support the following:
#  SinglyLinkedList() Initializes the SinglyLinkedList object.

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # todo :  get(index)
  #  Get the value of the indexth node.If the index is invalid, return -1.
  # todo complixity  get(index):
  #  time = o(index)=(n), space=o(1)
  def get(self, index):
    if index < 0 or index >= self.size:
      return -1
    counter = 0
    current = self.head
    while counter != index:
      current = current.next
      counter += 1
    return current

  # todo :  addAtHead(value)-
  #  Add a node of given value before the first element of the linked list.
  # todo complixity  addAtHead(value):
  #  time = o(1), space=o(1)

  def addAtHead(self, value):
    node = Node(value)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head = node
    self.size += 1
    return self

  # todo :addAtTail(value) -
  #  Add a node of given value at the last element of the linked list.
  # todo complixity  addAtTail(value):
  #  time = o(1), space=o(1)
  def addAtTail(self, value):
    node = Node(value)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    self.size += 1
    return self

  # todo :  addAtIndex(index, value)
  #  Add a node of given value before the indexth node in the linked list.
  #  If index equals the length of the linked list,
  #  the node will be appended to the end of the linked list.
  #  If index is greater than the length, don’t insert the node.
  # todo complixity  addAtIndex(index,value):
  #  worst case:time =o(n), space=o(1)
  def addAtIndex(self, index, value):
    if index < 0 or index > self.size:
      return 'invalid index' 
    if index == self.size:
      return self.addAtTail(value)
    if index == 0:
      return self.addAtHead(value)
    node = Node(value)
    if index == self.size - 1:
      node.next = self.tail
      self.tail = node
    else:
      prev = self.get(index - 1)
      temp = prev.next
      prev.next = node
      node.next = temp
    self.size += 1
    return self

  # todo :deleteAtIndex(index) :
  #  Delete the indexth node in the linked list,
  #  if the index is valid, else nothing happens.
  # todo complixity  DeleteAtindex(index):
  #  best time = o(1), space=o(1)
  #  worst time = o(1)
  def deleteAtIndex(self, index):
    if index < 0 or index >= self.size:
      return 'invalid index'
    if index == 0:
      temp = self.head
      self.head = temp.next
      self.size -= 1
      if self.size == 0:
        self.tail = None
      return temp.value
    if index == self.size - 1:
      oldTail = self.tail
      newTail = self.get(index - 1)
      self.tail = newTail
      newTail.next = None
      self.size -= 1
      return oldTail
    prev = self.get(index - 1)
    deletedNode = prev.next
    prev.next = deletedNode.next
    self.size -= 1
    return deletedNode

  def printNodes(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next


sl = SinglyLinkedList()
sl.addAtHead(1)
sl.addAtTail(2)
sl.addAtIndex(2, 3)

# Print the nodes
sl.printNodes()


