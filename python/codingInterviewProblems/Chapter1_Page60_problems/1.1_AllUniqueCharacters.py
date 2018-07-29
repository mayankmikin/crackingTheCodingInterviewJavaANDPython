from collections import defaultdict



def check_duplicates(str1):
    print ("for input :"+str1)
    duplicates_found=False
    for letter in str1:
        if str1.count(letter)>1:
            print ("duplicates found")
            duplicates_found=True
            break
    if not(duplicates_found):
        print ("no duplicates")

def check_duplicates_withDataStructure(str_):
    print ("check_duplicates_withDataStructure for input :"+str_)
    if(len(str_)==len(set(str_))):
        print("no duplicates")
    else:
        print("duplicates_found")

def check_duplicates_withDataStructureAndPrintOnlyDuplicateCharacters(str_):
    print ("check_duplicates_withDataStructureAndPrintOnlyDuplicateCharacters for input :"+str_)
    for letter in set(str_):
        if(str_.count(letter)>1):
            print("character "+letter+" is a duplicate with count",str_.count(letter))




# str="abcd" will return true
# str="aabcd" will retun false as 'aa' is not unique or disctinct
if __name__ == '__main__':
    #With data structures
    str1="abcd"
    str2="aabcd"
    #https://snakify.org/en/lessons/strings_str/
    # read Slices: subsequence
    #A=set(str1[::]) #this will get me all individual characters
    #print (A)
    check_duplicates(str1)
    check_duplicates(str2)
    check_duplicates_withDataStructure(str1)
    check_duplicates_withDataStructure(str2)
    check_duplicates_withDataStructureAndPrintOnlyDuplicateCharacters(str1)
    check_duplicates_withDataStructureAndPrintOnlyDuplicateCharacters(str2)
