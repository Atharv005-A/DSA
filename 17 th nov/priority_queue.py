# Priority Queue using Singly Linked List 
class Node:
    def __init__(self, value, priority):
        self.data = value
        self.priority = priority
        self.next = None
        
class PriorityQueue:
    def __init__(self):
        self.front = None
    
    def enqueue(self, newnode):
        if self.front is None:
            self.front = newnode
            return

        if self.front.priority > newnode.priority:
            newnode.next = self.front
            self.front = newnode
            return

        temp = self.front
        while temp.next and newnode.priority >= temp.next.priority:
            temp = temp.next

        newnode.next = temp.next
        temp.next = newnode

    def dequeue(self):
        if self.front is None:
            return 
        self.front = self.front.next
            
    def printdata(self):
        if self.front is None:
            return "Queue is Empty!"
        
        temp = self.front
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()

pq = PriorityQueue()
pq.enqueue(Node(4, 1))
pq.enqueue(Node(5, 2))
pq.enqueue(Node(6, 3))
pq.enqueue(Node(7, 0))
pq.printdata()
pq.dequeue()
pq.printdata()
pq.dequeue()
pq.printdata()
pq.dequeue()
pq.printdata()
pq.dequeue()
pq.printdata()