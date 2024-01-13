#todo: (Sorting Algorithms):
# Question 2:Radix Sort-
# You are given an array of non-negative integers.
# Write a function that will take this array as input and
# return the sorted array using Radix sort.

 #todo 2 : complexity time : # time= o(d*(n+k)) space=o(n+k)
# d= hundredth-tenth-unit=241
# k=0,1,2,3....,9
#n=len(array)
# k increase then d decrease --->
# k =10  (0 to 9 ---> 50 --->  d=2
# k=2 (0 to 1) -----> 110010-----> d=6
#todo: method 1:
import math
def Radix_sort(array):
    if len(array)==0 :
      return  print("array is empty")
    greatestNumber = max(array)
    numberOfDifits= int(math.log10(greatestNumber)+1)

    #counting sort has to be done x nunmber of times where x=numberOfDidits
    for i in range(0,numberOfDifits):
      countingSort( array,i)
    return array
def countingSort(array, place):
  output= [0]*len(array)
  temp = [0]*10
  digitPlace = 10**place  ## Convert to integer using exponentiation

  for num in array:
    digit = (num // digitPlace) % 10
    temp[digit] += 1

  for i in range(1, 10):
    temp[i]= temp[i]+temp[i-1]


  for j in range(len(array) -1, -1, -1):
    currDigit = (array[j]//digitPlace) % 10
    temp[currDigit] -= 1
    insertPostion = temp[currDigit]
    output[insertPostion] = array[j]

  for i in range(len(array)):
    array[i] = output[i]

print("original list",[384,73,374,183,65,247,185])
print("sorted list:", Radix_sort([384,73,374,183,65,247,185]))

#todo: method 2:
def radixSort(array):
  if len(array) == 0:
    return 'empty array'
  greatestNumber = max(array)
  numberOfDigits = len(str(greatestNumber))
  for i in range(numberOfDigits):
    countingSort(array, i)
  return array


def countingSort(array, place):
  output = [0] * len(array)
  temp = [0] * 10
  digitPlace = 10 ** place
  for num in array:
    digit = (num // digitPlace) % 10
    temp[digit] += 1
  for i in range(1, 10):
    temp[i] += temp[i - 1]
  for j in range(len(array) - 1, -1, -1):
    currDigit = (array[j] // digitPlace) % 10
    temp[currDigit] -= 1
    insertPosition = temp[currDigit]
    output[insertPosition] = array[j]
  array[:] = output

print("original list_method2",[384,73,374,183,65,247,185])
print("sorted list:method 2", Radix_sort([384,73,374,183,65,247,185]))

#todo: method 3:
def radix_sort(array):
  if not array:
    return array

  max_num = max(array)
  exp = 1
  n = len(array)

  output = [0] * n

  while max_num // exp > 0:
    count = [0] * 10
    for i in range(n):
      count[(array[i] // exp) % 10] += 1

    for i in range(1, 10):
      count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
      output[count[(array[i] // exp) % 10] - 1] = array[i]
      count[(array[i] // exp) % 10] -= 1

    for i in range(n):
      array[i] = output[i]

    exp *= 10

  return array


