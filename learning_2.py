#-------------------reverse a string----------------------------#
def reverse_string(string):
    return string[::-1]

# Test the function
print(reverse_string("enthada mone"))  

# Output: "olleh"



#----------------------palindrome----------------------------------#

def is_palindrome(string):
    return string == string[::-1]

# Test the function
print(is_palindrome("racecar")) 
 # Output: True
print(is_palindrome("enthada mone"))    
# Output: False

#-----------------factorial of a number------------------------------#
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
print(factorial(5))  

# Output: 120

