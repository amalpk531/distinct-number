
n = int(input("Enter the number of elements: "))
elements = []
for i in range(n):
    element = int(input("Enter element: "))
    elements.append(element)
elements.sort()
print("The second largest number is:", elements[-2])

