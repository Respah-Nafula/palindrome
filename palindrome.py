def string_palindrome(string):
    left = 0 
    right = len(string)-1
    while left < right:
        
        if string[left] != string[right]:
            print("String not a palindrome")
            break
        else:
            left += 1        
            right -= 1
        print ("The string is a palindrome" )
string_palindrome("ken")
       
       