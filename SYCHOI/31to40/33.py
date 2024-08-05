# 리스트 형식의 result를 전역변수로 생성했었음. 하지만 파이썬에서는 전역변수를 사용할 때 매 함수마다 'global 전역변수명' 형식으로 호출해줘야 하기 때문에 번거로움. 그냥 함수의 매개변수로 호출

def find(result, x) :           # x가 속한 집합의 대표 원소(Root) 찾기
    if result[x] == x :
        return result[x]        # 인덱스 값 == 노드 값 : 부모 노드(Root)
    
    parent = find(result, result[x])         # 인덱스 값 != 노드 값 : 자식 노드 => 부모노드 찾기(재귀함수)
    return parent

def union(result, x, y) :       # x와 y가 속한 두 집합 합치기
    root1 = find(result, x)
    root2 = find(result, y)     # 각 노드(x, y)가 속한 집합의 루트 노드 찾기

    result[root2] = root1   # y가 속한 집합의 루트노드(root2)를 x가 속한 집합의 루트노드(root1)와 합치기


def solution(k, operations) :
    # 노드의 값 : 인덱스 , 부모노드 : 리스트 값
    result = list(range(k))     # 처음에는 각 노드가 자기 자신을 부모로 가지도록 초기화
    n = k

    for lst in operations :
        if lst[0] == 'u' :
            union(result, lst[1], lst[2])
            # print(lst[0], lst[1], lst[2])
        # elif lst[0] == 'f' :
        #     root = find(lst[1])
            # print(lst[0], lst[1])
    
    n = len(set(find(result, i) for i in range(k)))
    return n

#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution(3, [['u', 0, 1], ['u', 1, 2], ['f', 2]]))
# print(solution(4, [['u', 0, 1], ['u', 2, 3], ['f', 0]]))