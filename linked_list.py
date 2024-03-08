class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Taking input for linked list elements....
        
        
ll = LinkedList()
num_elements = int(input("Enter the number of elements: "))
for _ in range(num_elements):
    element = int(input("Enter element: "))
    ll.append(element)

# Displaying the linked list.....
ll.display()