def solution(answers) :
    cor = [0,0,0]   # [0] * 3
    listA = [1,2,3,4,5]             # 수포자1의 패턴
    listB = [2,1,2,3,2,4,2,5]       # 수포자2의 패턴
    listC = [3,3,1,1,2,2,4,4,5,5]   # 수포자3의 패턴

    for i in range(len(answers)) :
        if answers[i] == listA[i%4] :
            cor[0] += 1
        if answers[i] == listB[i%7] :
            cor[1] += 1
        if answers[i] == listC[i%9] :
            cor[2] += 1

    result = []
    for i in range(len(cor)) :  
        if cor[i] == max(cor) :     # 최대값이 2개 이상일 때
            result.append(i+1)      # 해당 값들의 인덱스+1 값을 result 리스트에 저장
    
    return result
    

#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))