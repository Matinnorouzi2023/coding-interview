
#Todo Question 1:(Sorting Algorithms):Bubble Sort
# - You are given an array of integers.
# Write a function that will take this array as input and return
# the sorted array using Bubble sort

def bubble_sort(array):
   sorted= False
   counter = 0
   while not sorted:
     sorted = True
     for i in range(len(array)-1-counter):
       if array[i]>array[i+1]:
         array[i], array[i+1]= array[i+1], array[i]
         sorted = False
     counter += 1
   return array
print(bubble_sort([1,2,3,4,0]))

#TODO: T=(N^2)= 1+2+2+...N= N(N+1)/2:  S=(1)


