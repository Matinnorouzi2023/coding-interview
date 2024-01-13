# todo: (Singly Linked List):-Linked List Data Structure Crash Course
#  Question 2:delete duplicates -
#  You are given the head of a Sorted Singly Linked list.
#  Write a function that will take the given head as input,
#  delete all nodes that have a value that is already the value of another node
#  so that each value appears 1 time only and return the linked list,
#  which is still to be a sorted linked list.

# todo complixity  get(index):
#  time = o(index)=(n), space=o(1)
#
# todo complixity  addAtHead(value):
#  time = o(1), space=o(1)





class Node:
  def __init__(self, value):
    self.val = value
    self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node('a')
head.next.next.next.next.next = Node('a')


def removeDupes(head):
  curr = head
  while curr:
    nextDistinctVal = curr.next
    while nextDistinctVal is not None and curr.val == nextDistinctVal.val:
      nextDistinctVal = nextDistinctVal.next
    curr.next = nextDistinctVal
    curr = nextDistinctVal
  return head


removeDupes(head)