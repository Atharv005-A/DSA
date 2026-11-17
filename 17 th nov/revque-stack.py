class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def print_stack(self, temp):
        while temp:
            print(temp.data)
            temp = temp.next


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear:
            self.rear.next = new_node
            self.rear = self.rear.next
        else:
            self.front = self.rear = new_node

    def print(self):
        temp = self.front

        while temp:
            print(temp.data)
            temp = temp.next

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            temp.next = None
            return temp
        else:
            print("Queue is empty")
            return None

    def revstack(self):
        st = Stack()

        while self.front is not None:
            st.push(self.dequeue())

        while st.top is not None:
            temp = st.top
            st.top = st.top.next
            temp.next = None
            self.enqueue(temp.data)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Original Queue:")
q.print()

q.revstack()

print("Reversed Queue:")
q.print()