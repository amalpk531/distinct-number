def bubble_sort(arr):
    n = len(arr)
    

    for i in range(n):
       
        for j in range(0, n-i-1):
           
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Input from the user
arr = input("Enter elements separated by space: ").split()
arr = [int(num) for num in arr]

# Sorting using bubble sort
bubble_sort(arr)
print("Sorted array is:", arr)


#---------------------selection sort---------------------#


def selection_sort(array):
    n = len(array)
    
    # Traverse through all array elements..
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]

# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
selection_sort(array)
print("Sorted array is:", array)

