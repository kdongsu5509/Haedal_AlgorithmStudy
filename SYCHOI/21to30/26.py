def inorder(nodes, length) :
    res = ""
    if length < len(nodes) :
        res += inorder(nodes, length*2+1)    # 왼쪽 자식노드 방문
        res += str(nodes[length]) + " "     # 현재 노드 출력        # 출력에 노드 사이에 공백이 있으므로 공백 넣기
        res += inorder(nodes, length*2+2)    # 오른쪽 자식노드 방문
        return res
    else :
        return ""
    
def preorder(nodes, length) :
    res = ""
    if length < len(nodes) :
        res += str(nodes[length]) + " "         # 현재 노드 출력
        res += preorder(nodes, length*2+1)       # 왼쪽 자식노드 방문
        res += preorder(nodes, length*2+2)       # 오른쪽 자식노드 방문
        return res
    else :
        return ""

def postorder(nodes, length) :
    res = ""
    if length < len(nodes) :
        res += postorder(nodes, length*2+1)      # 왼쪽 자식노드 방문
        res += postorder(nodes, length*2+2)      # 오른쪽 자식노드 방문
        res += str(nodes[length]) + " "         # 현재 노드 출력
        return res
    else :
        return ""

def solution(nodes) :
    return [
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1]        # 각 함수에서 res 문자열의 마지막 공백은 출력하면 안된다
    ]


#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([1, 2, 3, 4, 5, 6, 7]))