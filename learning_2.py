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
#--------------------leap year-----------------------------------#
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")

