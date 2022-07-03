class Node:
    def __init__(self,item):
        self.data=item
        self.prev=None
        self.next=None
        

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount=0
        self.head=Node(None)
        self.tail=Node(None)
        #dummyCode 생성
        self.head.prev=None
        self.head.next=self.tail
        self.tail.prev=self.head
        self.tail.next=None
    
    def traverse(self):
        result=[]
        curr=self.head
        while curr.next.next:
            curr=curr.next
            result.append(curr.data)
        return result
    
    def getAt(self,pos):
        if pos<0 or pos>self.nodeCount:
            return None
        
        #양방향이니까 tail부터 오는게 효율성 좋음
        if pos>self.nodeCount//2:
            i=0
            curr=self.tail
            while i<self.nodeCount-pos+1: #nodeCount=10 pos 8이면? 
                curr=curr.prev
                i+=1
        else:
            i=0
            curr=self.head
            while i<pos:
                 curr=curr.next
                 i+=1
                 
        return curr
    
    
    def insertAfter(self,prev,newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True
    
    
    def insertAt(self,pos,newNode):
        
        if pos<1 or  pos>self.nodeCount+1:
            return False
        
        prev=self.getAt(pos-1)
       # print(prev)
        return self.insertAfter(prev,newNode)
    
    
    def popAfter(self, prev):
        #prev에서 주어진 node의 다음에 있던 node 삭제
        
        curr=prev.next
        next=curr.next
        prev.next=next
        next.prev=prev
        self.nodeCount-=1
        
        return curr.data
    
    
    
    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data
    
    
    def popAt(self, pos):
        #pos에 의하여 지정되는 node 삭제
       if pos<0 or pos>self.nodeCount:
           raise IndexError
           
       next=self.getAt(pos-1)
       return self.popAfter(next)
   
    
def solution(x):
    return 0
