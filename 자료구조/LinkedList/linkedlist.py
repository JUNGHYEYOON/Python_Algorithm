class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class LinkedList:
    def __init__(self):
        self.nodeCount=0
        self.head=None
        self.tail=None
        
    def getAt(self,pos): #pos번째에 있는 node를 반환하는 것
        #pos는 여기서 위치를 의미
        
        #pos가 linkedlist범위를 넘어가면
        if pos<1 or pos>self.nodeCount:
            return None
        
        curr=self.head
        i=1
        
        while i<pos: 
            i+=1
            curr=curr.next
        return curr
    
    def repr(self):
       if self.nodeCount == 0:
           return 'LinkedList: empty'

       s = ''
       curr = self.head
       while curr is not None:
           s += repr(curr.data)
           if curr.next is not None:
               s += ' -> '
           curr = curr.next
       #print(s)
       return s
    
    def traverse(self): #결과 출력
        curr=self.head
        array=[]
        
        while curr != None:
            array.append(curr.data)
            curr=curr.next
        print(array)
        return array
    
    def insertAt(self,pos,newnode):
        
        #insert하려는 위치가 말도안되는 경우
        if pos<1 or pos>self.nodeCount+1:
            return False
        
        #insert하려는 위치가 처음인 경우
        if pos == 1 :
            newnode.next=self.head #새노드는 원래 head를 가르키고
            self.head=newnode #head를 새노드로 바꾸기
        
        else:
            prev=self.getAt(pos-1)
            newnode.next=prev.next
            prev.next=newnode
        
        if pos==self.nodeCount+1:
            self.tail=newnode
        self.nodeCount+=1
    
    def popAt(self,pos):
        
        if pos<1 or pos>=self.nodeCount+1:
            raise IndexError
            
        curr=self.getAt(pos)
        prev=self.getAt(pos-1)
        
        if pos==1:
            if self.nodeCount==1:
                self.head=None
                self.tail=None
            else:
                self.head=self.getAt(pos+1)
        else:
            if pos==self.nodeCount:
                self.tail=prev
                prev.next=None
            else:
                prev.next=self.getAt(pos+1)
        self.nodeCount-=1
        
        return curr.data
    
    def solution(x):
        return 0
    
a=Node(67)
b=Node(34)
c=Node(28)
L=LinkedList()

L.insertAt(1,a)
L.insertAt(2,b)
L.insertAt(3,c)

L.traverse()


L.popAt(2)
L.traverse()
#print(L)
