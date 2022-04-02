class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        append_node = Node(value)
        if self.head is None:
            self.head = append_node
            self.tail = append_node
        else:
            self.tail.next = append_node
            self.tail= append_node
        self.length+=1
        return True

    def prepend(self,value):
        prepend_node = Node(value)
        if self.length == 0:
            self.head = prepend_node
            self.tail = prepend_node
        else:
            prepend_node.next = self.head
            self.head= prepend_node
        self.length+=1
        return True


my_linked_list = LinkedList(2)

my_linked_list.append(3)
print("List before prepend: ")
my_linked_list.print_list()
print("Head: ",my_linked_list.head.value)
print("Tail: ",my_linked_list.tail.value)

my_linked_list.prepend(1)
print("List after prepend: ")
my_linked_list.print_list()
print("Head: ",my_linked_list.head.value)
print("Tail: ",my_linked_list.tail.value)

    
