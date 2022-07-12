class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        '''
        중위순회: 왼쪽 하위 트리를 방문 후 root 방문 후 오른쪽 하위 트리 방문
        왼쪽-루트-오른쪽
        '''
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def preorder(self):
        '''
        전위순회: root를 먼저 방문
        그 뒤 왼쪽 하위 트리 모두 방문 후 오른쪽!
        루트-왼쪽-오른쪽
        '''
        traversal=[]
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
      

    def postorder(self):
        '''
        후위트리: 하위 트리 모두 방문 후 root 방문
        왼쪽-오른쪽-루트
        '''
        traversal=[]
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal
    
class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []


def solution(x):
    return 0