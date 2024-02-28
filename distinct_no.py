# Initialize an empty set to store distinct numbers
distinct_numbers = set()

# Get the number of elements from the user
num_elements = int(input("Enter the number of elements: "))

# Iterate through each number entered by the user
for i in range(num_elements):
    num = int(input("Enter number: ".format(i+1)))
    distinct_numbers.add(num)

print("Distinct numbers entered by the user are:")
for num in distinct_numbers:
    print(num)
