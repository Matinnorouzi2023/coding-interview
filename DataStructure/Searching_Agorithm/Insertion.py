
#Todo Question 2:(Sorting Algorithms):Insertion Sort
# You are given an array of integers.
# Write a function that will take this array as input and return
# the sorted array using Insertion sort

#todo: method1
def inseration_sort(array):

  for i in range(1,len(array)):
    j=i-1
    temp = array[i]
    while j>=0 and array[j]>temp:
      array[j+1] = array[j]
      j -= 1
    array[j+1] = temp
    return array

print(inseration_sort([5,7,1,3,2]))


#todo: method2
from random import randint as rnd
import matplotlib.pyplot as plt
amount = 10
_list= [rnd(1, amount) for i in range(amount)]
# shuffle(array_to_sort)
print(_list)
for i in range(1,amount):
  for j in range(i):
    if _list[j] > _list[i]:
      temp= _list[i]
      del _list[i]
      _list.insert(j, temp)
      break

  plt.bar(range(amount), _list)
  plt.pause(0.005)
  plt.clf()
plt.bar(range(amount), _list)
plt.show()


print("original list:", _list)
inseration_sort(_list)
print("sorted list", _list)



#todo : Best time(sorted)= O(n) .....
# worst_time=1+2+3+...+ n-1 =n(n-1)/2=o(n^2) ......
# Avg= o(n^2) ....
# space =o(1)---> not auxilary space

#todo: method3
from random import shuffle
amount = 10
_list = [i for i in range(amount)]
shuffle(_list)

# from random import randint as rnd
# amount = 10
# _list = [rnd(1, amount) for i in range(amount)]

for i in range(1, amount):
  for j in range(i):
      if _list[j] > _list[i]:
        item = _list[i]
        _list.pop(i)
        _list.insert(j,item)
print(_list)


