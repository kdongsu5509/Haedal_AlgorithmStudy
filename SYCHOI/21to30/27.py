# 포인터 Node 만드는 방법(class Node)와 이진탐색트리 만드는 방법(class BST)는 반드시 익혀두기!!

class Node :    # 포인터로 트리 표현하기
    def __init__(self, key) :   # 클래스의 첫 def(__init__)의 첫번째 인수는 무조건 self임. 호출 시 사용x
        self.left = None        # 왼쪽 자식 노드
        self.right = None       # 오른쪽 자식 노드
        self.val = key          # 현재 노드의 값

class BST :     # Binary Search Tree
    def __init__(self) :
        self.root = None

    # Binary Search Tree(이진탐색트리) 만드는 함수
    def insert(self, key) :         # key == 추가하려고 하는 값
        if not self.root :          # self.root가 없으면
            self.root = Node(key)   # 'Node' 클래스를 통해 self.root 선언
        else :                      # self.root가 있으면
            curr = self.root        # curr에 self.root 값 저장
            while True :
                if key < curr.val :                 # key 값이 BST의 현재 값보다 작으면
                    if curr.left :
                        curr = curr.left            # 왼쪽 노드가 있으면 현재 값 = 왼쪽 노드 값
                    else :
                        curr.left = Node(key)       # 왼쪽 노드가 없으면 왼쪽 노드에 현재 값 넣은 노드 생성(break)
                        break
                else :                              # key 값이 BST의 현재 값보다 크면
                    if curr.right :
                        curr = curr.right           # 오른쪽 노드가 있으면 현재 값 = 오른쪽 노드 값
                    else :
                        curr.right = Node(key)      # 오른쪽 노드가 없으면 오른쪽 노드에 현재 값 넣은 노드 생성(break)
                        break

    # Binary Search Tree(이진탐색트리) 탐색하는 함수
    def search(self, key) :         # key == 찾으려고 하는 값
        curr = self.root            # 트리의 루트 값을 기본 값으로 설정
        while curr and curr.val != key :        # 현재 값(루트 값)이 key(찾는 값)가 아니면 실행
            if key < curr.val :                 
                curr = curr.left                # 찾는 값이 현재 값보다 작으면 왼쪽 노드로 이동
            else :
                curr = curr.right               # 찾는 값이 현재 값보다 크면 오른쪽 노드로 이동
        return curr         # while문을 벗어나면(현재 값 == 찾는 값) 현재 값 리턴
    
def solution(lst, search_lst) :
    idx = BST()     # idx에 BST 클래스 입력
    for n in lst :
        idx.insert(n)       # lst에 있는 값들을 순서대로 idx 클래스의 insert 함수로 추가
    
    result = []
    for m in search_lst :
        if idx.search(m) :
            result.append(True)
        else :
            result.append(False)
    
    return result
        

#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))
print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))