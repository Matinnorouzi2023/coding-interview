#todo:
# Question 1:Max Heap Construction
# Write a max Heap Class that supports the following:
# 1.Building a Max heap from an input array
# 2.Inserting integers in the Heap
# 3.Removing the Heap’s maximum / root value
# 4.Peeking at the Heap’s maximum / root value
# The Heap is to be represented in the form of an array.
class MaxBinaryHeap:
  def __init__(self):
    self.heap = []

  def build_heap(self, array):
    length = len(array)
    last_parent = length // 2 - 1
    for i in range(last_parent, -1, -1):
      self.bubble_down(array, i)
    self.heap = array
    return self

  def bubble_down(self, array, idx):
    length = len(array)
    current = array[idx]
    while True:
      left_child_idx = 2 * idx + 1
      right_child_idx = 2 * idx + 2
      left_child, right_child = None, None
      largest = None

      if left_child_idx < length:
        left_child = array[left_child_idx]
        if left_child > current:
          largest = left_child_idx

      if right_child_idx < length:
        right_child = array[right_child_idx]
        if (largest is None and right_child > current) or (
                largest is not None and right_child > left_child
        ):
          largest = right_child_idx

      if largest is None:
        break

      # swap values
      array[idx], array[largest] = array[largest], current
      idx = largest

  def extract_max(self):
    maximum_value = self.heap[0]
    last = self.heap.pop()
    if self.heap:
      self.heap[0] = last
      self.bubble_down(self.heap, 0)
    return maximum_value

  def insert(self, value):
    self.heap.append(value)
    self.bubble_up()
    return self

  def bubble_up(self):
    idx = len(self.heap) - 1
    value = self.heap[idx]
    while idx > 0:
      parent_idx = (idx - 1) // 2
      parent_value = self.heap[parent_idx]
      if value <= parent_value:
        break
      self.heap[parent_idx] = value
      self.heap[idx] = parent_value
      idx = parent_idx

  def peek(self):
    return self.heap[0]


# Example usage
heap = MaxBinaryHeap()
heap.build_heap([4, 7, 3, 0, 9, 3, 2, 6])
