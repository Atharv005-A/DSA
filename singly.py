class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SinglyLL:
    def __init__(self):
        self.size=0
        self.head=None
    
    def append(self,data):
        newnode=Node(data)
        self.size+=1
        if not self.head:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode

    def traverse(self):
        if not self.head:
            print("LL is empty")
            return
        print("List data:")
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    
    
    def insertAtPos(self, data, pos):
        if pos < 1 or pos > self.size + 1:
            print("\nInsertion not possible")
            return
        
        newnode = Node(data)
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            c = 1
            while c < pos - 1:
                temp = temp.next
                c += 1
            newnode.next = temp.next
            temp.next = newnode
        self.size += 1
        print("\nInsertion successful at pos:",pos)

    def middleNodeCounter(self):
        if self.head is None:
            print("\nLL is empty")
            return
        mid = self.size // 2
        temp=self.head
        while mid!=0:
            temp = temp.next
            mid -= 1
        print("\nMiddle Node Value:",temp.data)

    def middleNode2P(self):
        if self.head is None:
            print("Empty LL")
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Mid val:", slow.data)

    def deleteAtPos(self,pos):
        if pos<1 or pos>self.size or self.head==None:
            print("List Empty")
            return
        
        if pos==1:
            self.head=self.head.next
            self.size-=1
            return
        tc=self.head
        tpre=tc
        c=1
        while c<pos:
            tpre=tc
            tc=tc.next
            c+=1
        tpre.next=tc.next
        self.size-=1
        print("Deleted node at pos:",pos)

    def reverseList(self):
        if self.head==None:
            print("LL is empty. Cannot reverse")
            return

        pre=None
        crnt=self.head
        while crnt:
            nextnode=crnt.next
            crnt.next=pre
            pre=crnt
            crnt=nextnode
        self.head=pre
        print("\nList reversed")

    def sum2Consecutive(self):
        if self.head==None or self.head.next==None:
            print("\nInsufficient no. of nodes")
            return
        print("\nSum of every 2 consecutive nodes:")
        temp = self.head
        while temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp = temp.next

    def deleteFirstLastNode(self):
        if self.head == None or self.head.next==None:
            print("\ninsufficient nodes")
            return
        
        self.head=self.head.next
        
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None

sl=SinglyLL()
for i in range(1,7):
    sl.append(i)

sl.traverse()

sl.insertAtPos(10,3)
sl.traverse()

sl.middleNodeCounter()

sl.deleteAtPos(4)
sl.traverse()

sl.reverseList()
sl.traverse()

sl.sum2Consecutive()

sl.middleNodeCounter()