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

    def pop(self):
        # pre check
        if self.length == 0:
            return None
        # temp 2 pointers temp and pre
        temp = self.head # use as tail
        pre = self.head # use as pre tail node
        while(temp.next):
            pre = temp
            temp = temp.next
        # when reached the tail None(means nth)
        self.tail = pre
        self.tail.next = None
        # as removed one element substract one element count
        self.length -= 1
        # considering if we removed all the element, point head and tail to none
        if self.length == 0:
            self.head=None
            self.tail=None

        return temp.value


my_linked_list = LinkedList(1)
# print("Head: ",my_linked_list.head.value)

my_linked_list.append(2)
my_linked_list.print_list()
# print("Tail: ",my_linked_list.tail.value)

# remove 2 from the list
print(my_linked_list.pop())

# remove 1 from the list
print(my_linked_list.pop())

# nothing to remove 
print(my_linked_list.pop())

# nothing to remove 
print(my_linked_list.pop())
    
