class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return

        temp = self.head
        p = 0
        while p != position - 1:
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def delete(self, value):
        temp = self.head

        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

    def display_forward(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")



dll = DoublyLinkedList()
dll.insert(10, 0)
dll.insert(20, 1)
dll.insert(30, 2)
dll.insert(15, 1)
dll.delete(20)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()