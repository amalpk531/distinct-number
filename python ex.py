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

