class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None



# it adds element at the end
def addElementEnd(value, circularList):

    newNode = Node(value)

    if circularList.head is None:
        circularList.head = newNode
        newNode.next = newNode
        return
    current = circularList.head
    while current.next != circularList.head:
        current = current.next

    current.next = newNode
    newNode.next = circularList.head

    return


def elementCounter(circularList):

    current = circularList.head
    numberOfNodes = 1

    if circularList.head is None:
        numberOfNodes = 0
        return numberOfNodes

    while current.next != circularList.head:
        numberOfNodes += 1
        current = current.next

    return numberOfNodes


def addElementAtSpecificPlace(value, circularList, place):

    if place > elementCounter(circularList):
        return addElementEnd(value)
    newNode = Node(value)

    current = circularList.head
    counter = 1

    if counter == place:
        circularList.head = newNode
        newNode.next = current
        return

    while counter != (place - 1):
        counter += 1
        current = current.next

    newNode.next = current.next
    current.next = newNode

    return


listOfNodes = CircularList()
node1 = Node(10)
listOfNodes.head = node1

node2 = Node(20)

node1.next = node2
node2.next = node1

current = listOfNodes.head

while True:
    print(current.value)
    current = current.next

    if current == listOfNodes.head:
        break
