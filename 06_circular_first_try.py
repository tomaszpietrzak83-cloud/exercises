class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class CircularList:
    def __init__(self):
        self.head = None

list = CircularList()
node1 = Node(10)
list.head = node1

node2 = Node(20)

node1.next = node2
node2.next = node1

current = list.head

# it adds element at the end
def addingElement(value):
    
    newNode = Node(value)

    if list.head == None:
        list.head = newNode
        newNode.next = newNode
        return
    current = list.head
    while current.next != list.head:
        current = current.next
    
    current.next = newNode
    newNode.next = list.head

    return 
    
    




while True:
    print(current.value)
    current = current.next

    if current == list.head:
        break
