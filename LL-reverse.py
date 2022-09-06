class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __size__(self):
        return self.length

    def print_list(self):
        temp = self.head
        if temp is None:
            print("# Nth to print: List is empty!! ")

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        append_node = Node(value)
        if self.head is None:
            self.head = append_node
            self.tail = append_node
        else:
            self.tail.next = append_node
            self.tail = append_node
        self.length += 1
        return True

    def prepend(self, value):
        prepend_node = Node(value)
        if self.length == 0:
            self.head = prepend_node
            self.tail = prepend_node
        else:
            prepend_node.next = self.head
            self.head = prepend_node
        self.length += 1
        return True

    def pop(self):
        # pre check
        if self.length == 0:
            return None
        # temp 2 pointers temp and pre
        temp = self.head  # use as tail
        pre = self.head  # use as pre tail node
        while temp.next:
            pre = temp
            temp = temp.next
        # when reached the tail None(means nth)
        self.tail = pre
        self.tail.next = None
        # as removed one element subtract one element count
        self.length -= 1
        # considering if we removed all the element, point head and tail to none
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp  # always return the entire node only, for test we can use .value

    def pop_first_bad_one(self):
        if self.length == 0:
            return False
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp  # always return the entire node only, for test we can use .value

    def get(self, index):
        if index < 0 and index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 and index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if 0 > index >= self.length:
            return None
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next

        # prev.next = post  # free up the temp, remove it from prev next
        prev.next = temp.next  # free up the temp, remove it from prev next
        temp.next = None  # ready temp for gc as temp next is not pointing to None

        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print("List Looks like: ")
my_linked_list.print_list()
print("Head: ", my_linked_list.head.value)
print("Tail: ", my_linked_list.tail.value)
print("curr size: ", my_linked_list.length)

print("Reverse the list: ")
print(my_linked_list.reverse())
print("Now list look like this: ")
my_linked_list.print_list()
print("Head: ", my_linked_list.head.value)
print("Tail: ", my_linked_list.tail.value)
print("curr size: ", my_linked_list.length)
