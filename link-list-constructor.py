class Node:
    def __init__(self,value=None):
        if value is None:
            self.value = None
        else:
            self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
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


my_linked_list = LinkedList()
# print("Head: ",my_linked_list.head.value)

my_linked_list.append(6)
my_linked_list.print_list()
print("Tail: ",my_linked_list.tail.value)

    
