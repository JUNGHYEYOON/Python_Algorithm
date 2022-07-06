class ArrayStack:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self): 
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
def solution(expr):
    match={
        ')':'(',
        '}':'{',
        ']':'['}
  
    S=ArrayStack()
    
    for c in expr: 
        if c in'({[':
            S.push(c)
            #print(c)
        elif c in match:
            #만약 닫는 괄호가 있는데 여는 괄호 없어
            if S.size()==0:
                return False
            else:
                #닫는괄호 있어 근데 여는괄호랑 맞지 않아
                t=S.pop()       
                print(c)
                if t!=match.get(c):
                    '''
                    match.get(t)가 아닌 match.get(c)인 이유
                    여기서 c는 닫는 괄호들이니까 그거에대한 value값
                    '''
                    return False
    #그 외에 스택이 비어있다면 참        
    #그게 아니라면, 여닫는 괄호가 맞지 않는 거니까 틀림.
  
    return S.isEmpty()

                
solution('{(3+4)*5}*2')
        
        
        