def solution(id_list, report, k):
    total = [[0] * len(id_list) for x in range(len(id_list))]
    # part = [0] * len(id_list)
    
    user_dict = {}
    for i in range(len(id_list)):
        # total.append(part)
        user_dict[id_list[i]] = i
        
    for x in report:
        a,b = x.split()
        newA = user_dict[a]
        newB = user_dict[b]
        if(total[newA][newB] == 0):
            total[newA][newB] = 1
    # print(total)
        
    banned = []
    
    temp = 0
    # idx = 0
    for i in range(len(id_list)):
        for j in range(len(id_list)):
            if total[j][i] != 0:
                temp += 1
        if(temp >= k):
            banned.append(i)
            temp = 0
        else:
            temp = 0
#     print(total)
#     print(banned)
    
    mailing = [0] * len(id_list)
    #다시 완전 탐색 레츠 고릿
    for i in range(len(id_list)): #행 탐색.
        for j in banned:
            if total[i][j] != 0:
                mailing[i] += 1
    
    return mailing
# id_list = ["a", "b", "c", "d"] ;
# report = ["a b", "a b", "c a", "d a", "a b", "c d", "a d", "b c", "b a", "d a"];
# k = 2

# 기댓값 : [1, 1, 2, 1]