from random import shuffle

length=10
_list = [ i for i in range(length)]
shuffle(_list)
print("original list",_list)
n = len(_list)

output = [0] * n
print(output)

def initialize_to_zero(array):
  for i in range(len(array)):
    array[i] = 0
  return array

array = [1,2,3]
initialize_to_zero(array)
print(array)

# Output: [0, 0, 0]


import numpy as np

def initialize_to_zero_efficient(array):
  array[:] = 0
  return array
import numpy as np

array = np.array([1,2,3])
initialize_to_zero_efficient(array)
print(array)

# Output: [0 0 0]
