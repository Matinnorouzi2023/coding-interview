# TODO: Question 2:Group Anagrams -
#  Given an array of strings consisting of lower case English letters,
#  group the anagrams together. You can return the answer in any order.
#  An Anagram is a word or phrase formed by rearranging the letters
#  of a different word or phrase, using all the original letters exactly once.
#  Time= o(s*nlogn)= o(nlogn)
#      s--> number string .
#      n--->> max number of charachter
#      check if in hashtable - --> push----time=o(1)
#  space=o(s*n)
#      sorted array ===> s*n
#      output array ----> s*n
#      hash table----> s*n

def group_anagrams(strings):
    if len(strings) == 0:
      return []
    sorted_string = [''.join(sorted(i)) for i in strings]
    hash = {}
    for i in range(len(sorted_string)):
      if sorted_string[i] in hash:
        hash[sorted_string[i]].append(strings[i])
      else:
        hash[sorted_string[i]] = [strings[i]]
    return list(hash. values())

print(group_anagrams(['arc', 'abc', 'car','cat','act','acb','atc']))