def solution(answers) :
    cor = [0,0,0]
    listA = [1,2,3,4,5]
    listB = [2,1,2,3,2,4,2,5]
    listC = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)) :
        if answers[i] == listA[i%4] :
            cor[0] += 1
        if answers[i] == listB[i%7] :
            cor[1] += 1
        if answers[i] == listC[i%9] :
            cor[2] += 1

    result = []
    for i in range(len(cor)) :
        if cor[i] == max(cor) :
            result.append(i+1)
    
    return result
    

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))