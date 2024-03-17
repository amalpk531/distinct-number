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

#----------------------unique list----------------------------------#
		my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Remove duplicates using a set
unique_list = set(my_list)

print("The list with unique elements only:")
print(unique_list)

# output:The list with unique elements only:
#{1, 2, 4, 6, 9} """

#----------------------write in a file-----------------------#
# Create a new file called "myfile.txt" and write text to it
with open("myfile.txt", "w") as f:
  f.write("This is some new text for the file.")

print("Successfully wrote text to the file.")



