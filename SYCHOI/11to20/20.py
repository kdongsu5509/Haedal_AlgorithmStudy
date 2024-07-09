def solution(participant, completion) :
    name = {}

    for wordP in participant :
        if wordP in name :
            name[wordP] += 1
        else :
            name[wordP] = 1
    
    for wordC in completion :
        if wordC in name :
            name[wordC] -= 1
    
    for key in name :
        if name[key] != 0 :
            return key


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))