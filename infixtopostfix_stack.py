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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    '''
    수식에서 문자 하나씩 받기 
    -> 피연산자이면 출력, 연산자이면 stack에 저장
    주의)
    '''
    answer='' #문자열 
    opStack = ArrayStack()
    for c in S:
        if c in prec:
            #연산자인 경우에 stack에 넣기
            #근데, 괄호랑 우선순위 고려할 것
            '''
            만약 (면 무조건 넣고, 비어도 무조건 넣기
            만약에 연산자 또 들어오면 젤 위에 것이랑 비교해서 우선순위 높은거 '계속' 빼기
            만약에 )면 (까지 계속 pop
            '''
            if opStack.isEmpty():
                opStack.push(c)
            else:
                if c=='(':
                    opStack.push(c)
                elif prec.get(opStack.peek())>=prec.get(c):
                    #계속 빼야함
                    #A+B*C-D와 같은 경우 생각 못함
                        while (opStack.size()>0) and prec.get(opStack.peek())>=prec.get(c):
                            answer+=opStack.pop()
                            #print(answer)
                            #print(opStack.peek)
                        opStack.push(c)
                        
                else:
                    opStack.push(c)       
        else:
            #닫는 괄호
            if c ==')':
                while( opStack.peek()!='(' ):
                    answer+=opStack.pop()
                opStack.pop()
            #피연산자    
            else:
                answer+=c
    #S에 남은거 넣기
    while not opStack.isEmpty():
        answer+=opStack.pop()
    #print(answer)
    return answer
solution('a+b*c-d')