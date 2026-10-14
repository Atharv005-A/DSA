class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def traverse(self):
        values = []
        cur = self.head
        while cur:
            values.append(str(cur.data))
            cur = cur.next
        print("->".join(values) if values else "list is empty")

    def insert(self, pos, data):
        if pos < 0:
            print("invalid position") 
        node = Node(data)
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        cur = self.head
        for _ in range(pos - 1):
            if cur is None:
                break
            cur = cur.next
        if cur is None:
            print("invalid position")
            return 
        node.next = cur.next
        cur.next = node

    def find_middle(self):
        if self.head is None:
            print("list is empty")
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("middle", slow.data)
        return slow.data

    def delete(self, key):
        if self.head is None:
            print("list is empty")  # Fixed typo
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.data != key:
            cur = cur.next
        if cur.next is None:
            print(f"{key} not found")
        else:
            cur.next = cur.next.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def pair_sums(self):
        sums = []
        cur = self.head
        while cur:
            if cur.next:
                sums.append(cur.data + cur.next.data)
                cur = cur.next.next
            else:
                sums.append(cur.data)  
                cur = None
        print("pair sums:", sums)
        return sums

def solution():
    ll = SinglyLinkedList()
    ll.create([10, 20, 30, 40, 50])
    print("created:")
    ll.traverse()
    
    ll.insert(2, 25)
    print("after inserting 25 at position 2:")
    ll.traverse()
    
    ll.find_middle()
    
    ll.delete(40)
    print("after deleting 40:")
    ll.traverse()
    
    ll.reverse()
    print("after reversing:")
    ll.traverse()
    
    ll.pair_sums()

solution()
