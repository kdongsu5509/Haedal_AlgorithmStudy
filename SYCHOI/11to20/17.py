def solution(cards1, cards2, goal) :
    result = "Yes"
    for i in goal :     # i == i, want, to, drink, water
        # print("this time i == ", i)
        if cards1 and i == cards1[0] :
            # print(i, ": cards1에 있음")
            del(cards1[0])
            continue
        elif cards2 and i == cards2[0] :
            # print(i, ": cards2에 있음")
            del(cards2[0])
            continue
        else : 
            result = "No"
            return result       # 단어 배열 맞추기에 실패할 경우
        
    return result               # 단어 배열 맞추기에 성공한 경우(for문을 모두 순회함)
        


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
# print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))