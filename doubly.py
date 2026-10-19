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

    def print_reverse_recursive(self, node=None, is_start=True):
        if is_start:
            node = self.head
        if node is None:
            if is_start:
                print("None")
            return
        
        self.print_reverse_recursive(node.next, is_start=False)
        print(node.data, end=" <-> ")
        if is_start:
            print("None")

    def search_and_count(self, value):
        temp = self.head
        count = 0
        
        while temp is not None:
            if temp.data == value:
                count += 1
            temp = temp.next
            
        return count


# Execution
dll = DoublyLinkedList()
dll.insert(10, 0)
dll.insert(20, 1)
dll.insert(30, 2)
dll.insert(10, 3) # Inserting duplicate '10' for testing
dll.insert(15, 1)
dll.delete(20)

print("Current List:")
dll.display_forward()

# Testing search and count
search_val = 10
result = dll.search_and_count(search_val)
print(f"\nThe number {search_val} appears {result} time(s) in the list.")
