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
