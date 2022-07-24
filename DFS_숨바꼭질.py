'''
입력
수빈 위치:N 동생 위치: K

출력
동생을 찾는 가장 빠른 시간
'''

N,K=map(int,input().split())

ans=[]

if K>=N:
    ans.append(K-N)
else:
    ans.append(N-K)


def DFS(x,answer):

    
    #print('x',x,answer,min(ans))
    
    if answer > min(ans):
        return 
    
    if x==K and answer<min(ans):
        ans.append(answer)
        
    else:
        return DFS(x+1,answer+1),DFS(x-1,answer+1),DFS(2*x,answer+1)
   
DFS(N,0)
print(min(ans))



