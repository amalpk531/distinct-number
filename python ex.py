arr = input("Enter elements of the array separated by space: ").split()
arr = [int(x) for x in arr]  # Convert input elements to integers

# Question 1: Find the maximum element in an array

def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element
print("Maximum element in the array:", find_max(arr))

# Question 2: Reverse an array

def reverse_array(arr):
    return arr[::-1]
print("Reversed array:", reverse_array(arr))

# Question 3: Find the sum of elements in an array

def array_sum(arr):
    return sum(arr)
print("Sum of array elements:", array_sum(arr))

# Question 4: Check if an array is sorted

def is_sorted(arr):
    return arr == sorted(arr)
print("Is the array sorted?", is_sorted(arr))

# Question 5: Remove duplicates from an array

def remove_duplicates(arr):
    return list(set(arr))
print("Array after removing duplicates:", remove_duplicates(arr))
