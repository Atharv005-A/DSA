class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self, values):
        self.head = None
        tail = None

        for v in values:
            node = Node(v)

            if self.head is None:
                self.head = tail = node
            else:
                tail.next = node
                tail = node

        if tail:
            tail.next = self.head

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        cur = self.head
        while True:
            print(cur.data, end=" -> ")
            cur = cur.next

            if cur == self.head:
                break

        print("(back to head)")

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            node.next = self.head
            return

        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        cur.next = node
        node.next = self.head

    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
                return

            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            self.head = self.head.next
            cur.next = self.head
            return

        cur = self.head
        while cur.next != self.head and cur.next.data != key:
            cur = cur.next

        if cur.next == self.head:
            print(key, "not found")
        else:
            cur.next = cur.next.next


ll = CircularLinkedList()

ll.create([10, 20, 30, 40, 50])

print("Created list:")
ll.traverse()

ll.insert(60)
print("After inserting 60:")
ll.traverse()

ll.delete(30)
print("After deleting 30:")
ll.traverse()
