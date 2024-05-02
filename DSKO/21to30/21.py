import copy
def solution(want, number, discount):
    di = dict()
    for x in range(len(number)):
        di[want[x]] = x
    # print("di : ", di)
    li = [0] * len(number)
    for y in range(len(number)):
        li[y] = number[y]
    # print("li :", li)
    answer = 0
    
    
    for idx in range(0, len(discount) - 9):
        temp_li = copy.deepcopy(li)
        for i in range(idx, idx + 10):
            try:
                tk = discount[i]
                temp_li_idx = di[tk]
                if temp_li[temp_li_idx] > 0:
                    temp_li[temp_li_idx] -= 1
            except KeyError:
                continue
        if sum(temp_li) == 0:
            # print("idx : ", idx)
            # print("tempList : ", temp_li)
            # print("tempListSum : ", sum(temp_li))
            answer+=1
    return answer