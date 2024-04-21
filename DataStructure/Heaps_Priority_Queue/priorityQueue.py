#todo:Question 2:min Priority Queue Construction
# Implement a Priority Queue as a min Binary Heap.
# The Priority Queue class should support the following functions
# 1.Enqueue to insert an element
# 2.Dequeue to extract the element with the highest priority ( lowest numerical priority is treated as highest priority)


class Node:
  def __init__(self, value, priority):
    self.value = value
    self.priority = priority


class PriorityQueue:
  def __init__(self):
    self.data = []

  def enqueue(self, value, priority):
    node = Node(value, priority)
    self.data.append(node)
    self._bubble_up()
    return self

  def _bubble_up(self):
    idx = len(self.data) - 1
    element = self.data[idx]
    while idx > 0:
      parent_idx = (idx - 1) // 2
      parent = self.data[parent_idx]
      if element.priority >= parent.priority:
        break
      self.data[idx] = parent
      self.data[parent_idx] = element
      idx = parent_idx

  def dequeue(self):
    min_element = self.data[0]
    last = self.data.pop()
    if len(self.data) > 0:
      self.data[0] = last
      self._bubble_down()
    return min_element

  def _bubble_down(self):
    idx = 0
    length = len(self.data)
    element = self.data[0]
    while True:
      left_child_idx = 2 * idx + 1
      right_child_idx = 2 * idx + 2
      left_child, right_child = None, None
      smallest = None

      if left_child_idx < length:
        left_child = self.data[left_child_idx]
        if left_child.priority < element.priority:
          smallest = left_child_idx

      if right_child_idx < length:
        right_child = self.data[right_child_idx]
        if (
                (smallest is None and right_child.priority < element.priority)
                or (
                smallest is not None
                and right_child.priority < left_child.priority
        )
        ):
          smallest = right_child_idx

      if smallest is None:
        break

      self.data[idx] = self.data[smallest]
      self.data[smallest] = element
      idx = smallest


# Example usage
prior_queue = PriorityQueue()
prior_queue.enqueue("Job1", 3)
prior_queue.enqueue("Job2", 4)
prior_queue.enqueue("Job3", 1)
prior_queue.enqueue("Job4", 2)
prior_queue.enqueue("Job5", 1)

# Output:
# Job3 (priority 1)
# Job5 (priority 1)
# Job1 (priority 3)
# Job4 (priority 2)
# Job2 (priority 4)
