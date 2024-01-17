#todo:(Stacks):
# -Stacks Data Structure Crash Course
# Question 1:Construct Stack
# Implement a Stack:
# 1.Using an Array
# 2.with a Stack class using a Linked list
# One should be able to add to the stack and remove from the stack
# following the LIFO property.

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:
  def __init__(self):
    self.first = None
    self.last = None
    self.size = 0

  def add_at_beginning(self, value):
    new_node = Node(value)
    if not self.first:
      self.first = new_node
      self.last = new_node
    else:
      temp = self.first
      self.first = new_node
      new_node.next = temp
    self.size += 1
    return self

  def remove_from_beginning(self):
    if not self.first:
      return None
    temp = self.first
    self.first = self.first.next
    self.size -= 1
    if self.size == 0:
      self.last = None
    return temp


# Create a stack and add some nodes
stack = Stack()
stack.add_at_beginning(1)
stack.add_at_beginning(2)
stack.add_at_beginning(3)

# Remove a node from the beginning
removed_node = stack.remove_from_beginning()
print(f"Removed Node: {removed_node.value}")

# Output the current stack
current_node = stack.first
while current_node:
  print(current_node.value)
  current_node = current_node.next
