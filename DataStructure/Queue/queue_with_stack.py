#todo:
# Question 2:Implement Queue with Stack
# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of
# a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
# push(val) Pushes element val to the back of the queue.
# pop() Removes the element from the front of the queue and returns it.
# peek() Returns the element at the front of the queue.
# empty() Returns true if the queue is empty, false otherwise.
# Notes: You must use only standard operations of a stack,
# which means only push to top, peek/pop from top, size,
# and is empty operations are valid. Depending on your language,
# the stack may not be supported natively.
# You may simulate a stack using a list or deque (double-ended queue) as long as
# you use only a stack's standard operations.
# Follow-up: Implement the queue such that each operation
# is amortized O(1) time complexity. In other words,
# performing n operations will take overall O(n) time even if one of
# those operations may take longer.

class MyQueue:
  def __init__(self):
    self.in_stack = []
    self.out_stack = []

  def push(self, val):
    self.in_stack.append(val)

  def pop(self):
    if not self.out_stack:
      while self.in_stack:
        self.out_stack.append(self.in_stack.pop())
    return self.out_stack.pop() if self.out_stack else None

  def peek(self):
    if not self.out_stack:
      while self.in_stack:
        self.out_stack.append(self.in_stack.pop())
    return self.out_stack[-1] if self.out_stack else None

  def empty(self):
    in_stack_length = len(self.in_stack)
    out_stack_length = len(self.out_stack)
    return in_stack_length == 0 and out_stack_length == 0

  def print_queue(self):
    print("Queue:", self.in_stack + self.out_stack)


# Create a MyQueue instance
q = MyQueue()

# Perform some operations on the queue
q.push(1)
q.push(2)
q.push(3)
q.print_queue()

q.pop()
q.print_queue()
