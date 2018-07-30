import collections
#from collections import defaultdict

def checkPermutationsOfTwoStrings(str1,str2):
    print("solution of O(n(logn))")
    return ((len(str1)==len(str2))and(sorted(str1)==sorted(str2)))

# The idea is to add key of each character in the first string to the dictionary
# and increase it by 1 for each appearance. Then, for the second string, decrease
#  for each character’s appearance. In the last line, we return True only of all keys are equal to zero.
#  If not, we return False.
def checkPermutationsOfTwoStringsWithOneLoop(str1, str2):
    print("solution of O(n)")
    perm = collections.defaultdict(int)
    for char in str1:
        perm[char] += 1
    for char in str2:
        perm[char] -= 1
    return not any(perm.values())


if __name__ == '__main__':
    str1="hello"
    str2="lloeh"
    str3="hellow"
    print("checking if ",str1," is a permutation of ",str2," o/p: ",checkPermutationsOfTwoStrings(str1,str2))
    print("checking if ",str1," is a permutation of ",str3," o/p: ",checkPermutationsOfTwoStrings(str1,str3))
    print("checking if ",str1," is a permutation of ",str2," with one loop o/p: ",checkPermutationsOfTwoStringsWithOneLoop(str1,str2))
    print("checking if ",str1," is a permutation of ",str3," with one loop o/p: ",checkPermutationsOfTwoStringsWithOneLoop(str1,str3))


# we used ‘deafultdict’. It’s a subclass of ‘dict’ class and its functionality is very similar to a regular dict,
#  but there is one important difference between the two. If you’ll try to access non-existing key in a regular dict,
#  you’ll receive a KeyError exception, in ‘collections.defaultdict’ however, it will create the item you are trying to access.
#
# It does so by defining a new method called ‘__missing__’ and an instance variable called ‘default_factory’.
#  Everything else is inherited from the ‘dict’ class.
