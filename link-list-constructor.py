class Node:
    def __init__(self,value):
        self.value = value
        self.pointer = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


new_linkedList = LinkedList(5)
print(new_linkedList.head.value)
    
