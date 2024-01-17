#todo: Question 1:Construct Queue
# Implement a Queue:
# 1. Using an Array
# 2. with a Queue class using a Linked list
# One should be able to add to the queue and remove from the queue following the FIFO property.

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


# FIFO
class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.size = 0

  def enqueue(self, value):
    node = Node(value)
    if not self.first:
      self.first = node
      self.last = node
    else:
      self.last.next = node
      self.last = node
    self.size += 1
    return self

  def dequeue(self):
    if not self.first:
      return None
    temp = self.first
    self.first = self.first.next
    self.size -= 1
    if self.size == 0:
      self.last = None
    return temp

  def print_queue(self):
      current = self.first
      while current:
          print(current.value, end=" ")
          current = current.next
      print()
# Create a queue and enqueue values
queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
#queue1.dequeue()


queue1.print_queue()
