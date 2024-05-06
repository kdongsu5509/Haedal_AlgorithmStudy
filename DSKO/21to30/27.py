class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        #case1 : 트리가 비어잇을 때
        if not self.root:
            self.root = Node(key)

        #case2 : 트리가 비어있지 않을 때
        else:
            curr = self.root #이게 약간 커서 같은 느낌이네
            while True:
                #key값이 현재 노드의 값보다 작으면 왼쪽으로
                if key < curr.val:
                    #왼쪽에 노드가 있으면 왼쪽으로 이동
                    if curr.left:
                        curr = curr.left
                    #왼쪽에 노드가 없으면 새로운 노드를 만들고 종료
                    #structure 대신 클래스 사용했구나. class는 structure의 상위 호환이라는 것을 잊었네.
                    else:
                        curr.left = Node(key)
                        break
                #key값이 현재 노드의 값보다 크면 오른쪽으로
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(key)
                        break

    def search(self, key):
        curr = self.root
        while curr and curr.val != key:
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr is not None

def solution(lst, search_list):
    bst = BST()
    for i in lst:
        bst.insert(i)
    result = []
    for i in search_list:
        result.append(bst.search(i))
    return result

# Test cases
lst = [1, 3, 5, 7, 9]
search_list = [2, 4, 6, 8, 10]
print("Test case 1:", solution(lst, search_list))  # [False, False, False, False, False]

lst2 = [5, 3, 8, 4, 2, 1, 7, 10]
search_list2 = [1, 2, 5, 6]
print("Test case 2:", solution(lst2, search_list2))  # [True, True, True, False]
