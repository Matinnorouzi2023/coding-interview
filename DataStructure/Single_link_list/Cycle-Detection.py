#todo:(Linked Lists):
# Question 2:Cycle Detection - You are given the head of a linked list.
# Check if there is a cycle and if yes,  return the node where the cycle begins.
# If there is no cycle, return null. There is a cycle in a linked list
# if there is some node in the list that can be reached again by continuously
# following the next pointer. Do not modify the linked list.

#todo:method1:
# #Brut Force method:use hash table for visiting every nod
# time complexity = o(n)  s=(traverse n ) = o(n)

#todo:method2:
# #Floyd Algorithm
# T- tortoise ---> move 1 node(step)
# H- Hash ------- move 2 nodes(step)
# if H=T so there is a cycle then meet at the beging of cycle
# time complexity = o(n)  s=(1 ) 


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


def checkLoop(head):
  if not head:
    return None
  if not head.next:
    return None
  hare = head
  tortoise = head
  while hare and hare.next:
    hare = hare.next.next
    tortoise = tortoise.next
    if hare == tortoise:
      break
  if hare != tortoise:
    return None
  # find where cycle begins
  pointer = head
  while pointer != tortoise:
    pointer = pointer.next
    tortoise = tortoise.next
  return tortoise


# For Testing
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
# make a loop
six.next = three
head = one
checkLoop(head)

# Example usage:
# Constructing a linked list with a cycle
head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)
head.next.next.next.next = head.next  # Cycle

result = checkLoop(head)
if result:
    print("Cycle starts at node with value:", result.val)
else:
    print("No cycle in the linked list.")
