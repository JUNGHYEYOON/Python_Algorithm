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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            '''
            이 부분이 잘 이해가 안갔는데,
            두자릿수 연산을 위해 꼭 필요한 부분 
            예를들어, 32가 들어오면 3 따로 2따로 들어오는데 연속해서 들어오므로 두자릿수로 저장 가능
            '''
            val = val * 10 + int(c)
            #print(val)
            valProcessing = True
        else:
            if valProcessing: #tokens에 숫자 삽입
                tokens.append(val)
                val = 0 #이부분하지 않으면 숫자들이 계속 더해져서 들어오니까
            valProcessing = False
            tokens.append(c) #tokens에 연산자 삽입
     
    if valProcessing:
        tokens.append(val) #남은 거 삽입
    #print(tokens) 
    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for c in tokenList:
        #print(c)
        if c in prec:
            if opStack.isEmpty():
                opStack.push(c) 
            else:
                if c == '(':
                    opStack.push(c)
                elif prec.get(opStack.peek())>=prec.get(c):
                    while (opStack.size()>0) and prec.get(opStack.peek())>=prec.get(c):
                        postfixList.append(opStack.pop())
                    opStack.push(c)
                else: 
                    opStack.push(c)
        else:
            if c==')':
                while (opStack.data[-1]!='('):
                    postfixList+=opStack.pop()
                opStack.pop()
            else:
                postfixList.append(c)
                
                
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

        
    #print(postfixList)
    return postfixList


def postfixEval(tokenList):
    '''
    후위 표현식을 왼쪽부터 읽어서 피연사자면 stack에 넣기
    연산자면 stack에서 pop-> pop-> 연산한 후 다시 stack에 push
    '''
    valStack = ArrayStack()
    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        elif token=='*':
            a=valStack.pop()
            b=valStack.pop()
            valStack.push(a*b)
        elif token =='/':
            a=valStack.pop()
            b=valStack.pop()
            valStack.push(b/a)
        elif token=='+':
            a=valStack.pop()
            b=valStack.pop()
            valStack.push(a+b)
        elif token=='-':
            a=valStack.pop()
            b=valStack.pop()
            valStack.push(b-a)
    #print(valStack.pop())
    return valStack.pop()



def solution(expr):

    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
   # print(val)
    return val
    
solution('(3+2-4)*5')    
