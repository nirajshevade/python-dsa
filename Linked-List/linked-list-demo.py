class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Node1 = Node(10)
# Node2 = Node(20)
# Node3 = Node(30)
# Node4 = Node(40)
# Node5 = Node(50)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node5

n = int(input("Enter size of linked list: "))

head = tail = None

for i in range(n):
    data = int(input(f"Enter Data in  Node {i+1}: "))
    new_node = Node(data)
    
    if head is None:
        head = new_node
        tail = new_node
        
    else:
        tail.next = new_node
        tail = new_node

print("Linked List: ")
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print(None)

    