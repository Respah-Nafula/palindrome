my_str = 'mum'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

   # write a program to remove the panctuations from the string below

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char


print(no_punct)

# write a program to determine if given strings are anagram

str=input("Enter any string: ")
name=input("Enter any string: ")
str=str.lower()
name=name.lower()
if len(str)==(len(name)):
    sorted_str = sorted(str)
    sorted_name = sorted(name)
    if(sorted_str == sorted_name):
        print(str + " and " + name + " are anagrams.")
    else:
        print(str + " and " + name + " are not anagrams.")

else:
    print(str + " and " + name + " are not anagram.")



