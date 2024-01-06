# TODO: -
#  Question 2:Palindrome-You are given a string.
#  Write a function to check whether the string is a palindrome or not.

# TODO : METHOD1- create a new string and create an array of string
#  T=o(n^2)
#  S=o(n)
def is_palindrome(str):
  new_str = ''
  for i in reversed(range(len(str))):
    new_str += str [i]
  if str == new_str:
    return True
  return False


print(is_palindrome('aab'))

# TODO : METHOD2- push character in array- giving string and comvert to string
#  T=o(n)---> push element array which is constance
#  S=o(n)------> creating new array-- converting to string
def is_palindtome2(str):
    new_array = []
    for i in reversed(range(len(str))):
      new_array.append((str[i]))

    if(''.join(new_array) == str):
      return True
    return False


print(is_palindtome2('aabaa'))



# TODO : METHOD3- the best method
#  T=o(n/2)=o(n)---> travers once
#  S=o(1)
def is_palindrome3(str):
  i = 0
  j= len(str)-1
  while i<j:
    if str[i] != str[j]:
      return False
    i += 1
    j -= 1
  return True
print(is_palindrome3('abcba'))





