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
    
    def reverse(self):
        
        curr=self.tail
        array=[]
        
        while curr.prev.prev!= None:
            curr=curr.prev
            array.append(curr.data)
            
        #print(array)
        return array
    
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

    
    def insertbefore(self,next,newNode):
        #next는 어느 node의 앞에 새로운 node를 삽입할지
        
        prev = next.prev
        newNode.prev=prev
        newNode.next=next
        prev.next=newNode
        next.prev=newNode
        self.nodeCount+=1
        
        return True
    
    def insertAt(self,pos,newNode):
        
        if pos<1 or  pos>self.nodeCount+1:
            return False
        
        prev=self.getAt(pos-1)
       # print(prev)
        return self.insertAfter(prev,newNode)
    
    
    def popAfter(self, prev):
        #prev에서 주어진 node의 다음에 있던 node 삭제
        
        next=prev.next
        prev.next=next.next
        next.next.prev=prev
        self.nodeCount-=1
        
        return next.data
    
        '''
        dummynode가 존재하므로 이렇게 작성할 필요 없음
        next=prev.next
        if prev.next == None:
            return None
        else:
            if next.next==None:
                prev.next==None
                prev=self.tail
            else:
                prev.next=next.next
        '''        
      
         

    def popBefore(self, next):
        '''
        양방향이 가능하니까 앞에걸 삭제할 수 있음.
        '''
        #next에서 주어진 node의 이전에 있던 node 삭제
        #삭제되는 node에 담겨있던 data item return
        prev=next.prev
        #print(prev.data)
        next.prev=prev.prev
        prev.prev.next=next
        
        '''
        dummynode가 있어서 모든 node가 동일하므로 조건 안달아도 됨.
        if next.prev==None:
            return None
        else:
            if prev.prev==None:
                next.prev==None
                next=self.head
            else:
                next.prev=prev.prev
        '''       
        self.nodeCount -=1
        
        #print(next.data)
        return next.data  

    def popAt(self, pos):
        #pos에 의하여 지정되는 node 삭제
       if pos<1 or pos>self.nodeCount:
           raise IndexError
           
       next=self.getAt(pos-1)
       return self.popAfter(next)
           #pos가 뒷부분 위치하면 tail부터해서 posBefore로 삭제
    '''
           Q.이게 더 효율성이 높은 코드가 아닌가?
           A. 이미 get에서 둘을 나눠 놓았기 때문에 
           오히려 두개의 link를 따라가는 시간차만 발생한다.
           if pos>self.nodeCount//2:
               next=self.getAt(pos+1)
               print(next.data)
               return self.popBefore(next)
           
           else:
               prev=self.getAt(pos-1)
               return self.popAfter(prev)
           '''
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
        
        
def solution(x):
    return 0
    
L=DoublyLinkedList()
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)


L.insertAt(1,a)
L.insertAt(2,b)
L.insertAt(3,c)
L.insertAt(4,d)
L.insertAt(5,e)
L.insertAt(6,f)

print(L.traverse())
L.popAt(3)
print(L.traverse())
