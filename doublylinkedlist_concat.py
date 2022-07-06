
class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def concat(self, L):
        L1_tail=self.tail.prev
        L2_head=L.head.next
        
        if L1_tail != None and L2_head !=None:
            L1_tail.next=L2_head
            L2_head.prev=L1_tail
            self.tail=L.tail
        elif L1_tail is None:
            self.head=L2.head
            self.tail=L2.tail
        else:
            pass
        self.nodeCount+=L.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


def solution(x):
    return 0



L1=DoublyLinkedList()
L2=DoublyLinkedList()


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)


L1.insertAt(1,a)
L1.insertAt(2,b)
L1.insertAt(3,c)
print(L1.traverse())
L2.insertAt(1,d)
L2.insertAt(2,e)
L2.insertAt(3,f)
print(L2.traverse())
L1.concat(L2)
print(L1.traverse())