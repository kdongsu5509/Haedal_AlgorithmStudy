from collections import deque

class Node :
    def __init__(self, info, num, left=None, right=None) :
        self.info = info        # 노드의 좌표 정보
        self.left = left        # 노드의 왼쪽 자식 노드
        self.right = right      # 노드의 오른쪽 자식 노드
        self.num = num          # 노드의 번호

    def has_left(self) :
        return self.left is not None        # 왼쪽 노드에 값이 있으면 리턴
    
    def has_right(self) :
        return self.right is not None       # 오른쪽 노드에 값이 없으면 리턴


def make_BT(nodeinfo) :
    # 노드의 개수만큼 1부터 노드길이 + 1까지의 리스트 생성
    nodes = [i for i in range(1, len(nodeinfo) + 1)]
    
    # y좌표 내림차순 정렬, y좌표가 같을 때 x좌표 오름차순 정렬 (y축은 크고 x축은 작은 노드의 인덱스값 정렬)
    # nodes의 원소는 1부터, nodesinfo의 원소는 0부터 시작하므로 nodeinfo의 1차원 리스트에 대해서 x - 1 적용
    nodes.sort(key = lambda x : (nodeinfo[x - 1][1], -nodeinfo[x - 1][0]), reverse=True)
    root = None     # 루트 노드 초기화(None으로)

    # root를 기준으로 순회해서 트리에 노드 추가
    for i in range(len(nodes)) :
        if root is None :
            root = Node(nodeinfo[nodes[0] - 1], nodes[0])   # 'root' 노드의 info = nodeinfo[nodes[0] - 1], num = nodes[0]
        else :
            parent = root
            node = Node(nodeinfo[nodes[i] - 1], nodes[i])   # 자식 노드들의 info = nodeinfo[nodes[i] - 1], num = nodes[i]
        
            while True :
                # info[0] : 해당 노드(node, parent)의 x좌표
                if node.info[0] < parent.info[0] :      # parent의 x좌표가 node보다 크면
                    if parent.has_left() :
                        parent = parent.left                # parent의 왼쪽 노드에 값이 있으면 현재 parent를 parent의 왼쪽 노드로
                        continue
                    parent.left = node                      # parent의 왼쪽 노드에 값이 없으면 node 삽입
                    break
                else :                                  # node의 x좌표가 parent보다 크면
                    if parent.has_right() :             
                        parent = parent.right               # parent의 오른쪽 노드에 값이 있으면 현재 parent를 parent의 오른쪽 노드로
                        continue
                    parent.right = node                     # parent의 오른쪽 노드에 값이 없으면 node 삽입
                    break
    return root


def pre_order(root, answer) :   # 생성한 이진트리의 root, 전위순회를 담을 answer 리스트(answer[0])
    stack = [root]                      # stack에 root 노드 삽입
    while stack :
        node = stack.pop()              # stack의 최상단 노드 방문
        if node is None :               
            continue                    # 부모 노드의 왼쪽or오른쪽 노드가 없을 경우
        answer[0].append(node.num)      # 방문한 노드의 값 answer[0]에 append
        stack.append(node.right)
        stack.append(node.left)         # stack은 LIFO이기 때문에 먼저 방문할 왼쪽 노드를 나중에 삽입


def post_order(root, answer) :  # 생성한 이진트리의 root, 후위순회를 담을 answer 리스트(answer[1])
    stack = [(root, False)]             # stack에 root 노드 & 방문 여부 삽입
    while stack :
        node, visited = stack.pop()     # stack의 최상단 노드 방문
        if node is None :
            continue                    # 부모 노드의 왼쪽or오른쪽 노드가 없을 경우
        if visited :
            answer[1].append(node.num)  # 방문
        else :
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))




def solution(nodeinfo) :
    answer = [[], []]           # 이진 트리의 각각 [전위 순회], [후위 순회] 결과를 담을 변수
    root = make_BT(nodeinfo)    # 입력받은 노드의 좌표(nodeinfo)를 통해 이진 트리 생성
    pre_order(root, answer)
    post_order(root, answer)
    
    return answer


#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))