#todo: (Sorting Algorithms):
# Question 1:Quick Sort
# You are given an array of integers.
# Write a function that will take this array as input and
# return the sorted array using Quick sort..
# #
# todo2:time complexity:
#  BEST CASE=Average time=
#                               Time = o(nlogn)
#  Worst case =>n+ n-1  + n-2+ ...1=n(n+1)/2=n^2/2+n/2==>>
#                               Time = o(n^2)

#todo:space complexity:
# BEST CASE = Average time=     Time = o(logn)
#  Worst case =>                Time = o(n)


#todo: method1 :
from random import shuffle

length=10
_list = [ i for i in range(length)]
shuffle(_list)
print("original list",_list)

def quick_sort(_list, low, high):
     if low < high:
         pivot = low
         i = low
         j = high
         while i < j:
           while _list[i] <= _list[pivot] and i<j:
               i += 1
           while j>=0 and _list[j] >= _list[pivot]:
               j-=1
           if i < j:
                 _list[i],_list[j] = _list[j],_list[i]
         _list[j], _list[pivot] = _list[pivot], _list[j]

         quick_sort(_list,low,j-1)
         quick_sort(_list,j+1,high)

     return _list
sorted_list = quick_sort(_list,0,len(_list)-1)
print("sorted list:", sorted_list)



#todo: method2 :


from random import randint as rnd
length = 10
_list = [rnd(1,length) for i in range(length)]
print("original list",_list)

def quick_sort(_list):
  length = len(_list)
  if length <= 1:
    return _list
  else:
    pivot = _list.pop()
  right = []
  left = []
  for i in _list:
    if i < pivot:
      left.append(i)
    else:
      right.append(i)
  return  quick_sort(left) + [pivot] + quick_sort(right)

sorted_list =quick_sort(_list)
print("sorted list:", sorted_list)