
class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1 #-1로 초기화 했으므로, enqueue dequeue시 index를 0부터 이용 가능
        self.rear = -1
        '''
        *이때문에 front는 queue에서 가장 앞에 들어있는 원소(가장 먼저 삽입된 원소)를 갖는게 아니라
        그보다 하나 작은 index를 가짐.*
        '''

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear+1) % self.maxCount
        '''
        Circular Queue에서는 끝을만나면 다시 처음 위치로 돌아오게 되므로, 
        if를 사용하여 다시 돌아오게 할 수 있지만, self.rear의 값이 1씩 증가하다가
        self.maxCount의 값에 도달하면 0이 되도록 함으로써 원형 큐를 구현할 수 있음.
        '''
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.size()==0:
            raise IndexError('Queue empty')
       
        self.front = (self.front+1) % self.maxCount
        x = self.data[self.front] 
        self.count -= 1
       
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front+1)%self.maxCount]
        '''
         여기서 return값이 self.front가 아닌 이유
         -> front는 큐의 맨 앞에 있는(dequeue될) 원소보다 하나더 앞의 index
         -> rear는 마지막으로 삽입된(enqueue된) 원소가 저장된 index
         enqueue 연산에서는 rear를 먼저 증가시키고 나서 그 위치에 새 원소를 삽입하고
         dequeue 연산에서는 front를 먼저 증가시키고 나서 그 위치의 원소를 반환
         
        '''

def solution(x):
    return 0


