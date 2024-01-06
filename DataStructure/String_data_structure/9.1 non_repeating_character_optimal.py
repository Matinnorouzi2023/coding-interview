# TODO: -Strings Data Structure Crash Course
#  Question 1:Non repeating character -
#  You are given a string consisting of only lower case and upper-case English Alphabets and
#  integers 0 to 9. Write a function that will take this string as Input and return
#  the index of the first character that is non-repeating.
#  Method 1  : Brute Force Method:
#  Time = O(n^2)====> nested for loop(n character and n operation)
#  Space = O(1)

def non_repeating_chat(str):
  for i in range(len(str)):
    repeat = False
    for j in range(len(str)):
      if i!=j and str[i]== str[j]:
        repeat = True
    if repeat == False:
        return i
  return None

print(non_repeating_chat('abaRb150'))


class Solution(object):
  def firstUniqChar(self, s):
    for i in range(len(s)):
      repeat = False
      for j in range(len(s)):
        if i != j and s[i] == s[j]:
          repeat = True
      if not repeat:
        return i
    return -1  # Return -1 if no unique character is found


sol = Solution()
print(sol.firstUniqChar("abaRb150"))


# TODO:Method optimal manner- Using a hash table-
#  -------Time = o(n)   n operatipns hashtable and n travers string n+n =2n which is n
#  ------- Space =O(1)
def non_repeatind_char1(str):
    ht ={}
    for i in str:
      if i in ht:
          ht[i] += 1
      else:
          ht[i] = 1
    for i in range(len(str)):
      if ht[str[i]] == 1:
        return i
    return None
print(non_repeatind_char1('abaRb150'))

# TODO :Optimize_none_reapeating : with Brute-Force algorithm
#  Intuition
#  The intuition here is to keep track of the frequency of each character in
#  the string and then find the first character with a frequency of 1.
#  Approach
#  Utilize a hash table (dictionary in Python) to store the frequency of each character.
#  Iterate through the string to populate the hash table.
#  Iterate through the string again to find the first character with a frequency of 1.
#  Complexity
#  - Time complexity:
#  O(n) - We iterate through the string twice, and each iteration takes linear time.
#  - Space complexity:
#  O(n) - The space required for the hash table to store the frequency of each character. In the worst case, the hash table can have up to n entries, in this example is O(36)----> O(1)

# Code
class Solution(object):
    def firstUniqChar(self, s):
        ht ={}
        for i in s:
            if i in ht:
                ht[i] += 1
            else:
                  ht[i] = 1
        for i in range(len(s)):
             if ht[s[i]] == 1:
                return i
        return -1  # Return -1 if no unique character is found

sol = Solution()
print(sol.firstUniqChar("abaRb150"))
