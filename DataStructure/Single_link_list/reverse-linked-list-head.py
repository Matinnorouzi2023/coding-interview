#todo:(Linked Lists):
# Question 1:Reverse SLL-
# You are given the head of a Singly Linked list.
# Write a function that will take the given head as input,
# reverse the Linked List and return the new head of the reversed Linked List.
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


def printLinkedList(head):
  current = head
  while current:
    print(current.value, end=" ")
    current = current.next
  print()


def reverseLinkedList(head):
  prev = None
  current = head
  while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
  return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

reversed_head = reverseLinkedList(head)
printLinkedList(reversed_head)

#1--> none
#2---> 1--> none
#3---> 2---> 1--> none
#4 -->3---> 2---> 1--> none
#todo:time complexity= o(n) s=o(1)

