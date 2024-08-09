def solution(n, words) :
    result = []
    listUp = []
    idx = 1; round = 1; first = 1

    for word in words :
        if word in listUp :
            return [idx, round]     # 이미 나온 단어(listUp)가 나오면 리턴
        
        if first == 0 and word[0] != last :
            return [idx, round]     # (첫단어 제외) 이전 단어의 마지막 알파벳과 현재 단어의 첫 알파벳이 다르면 리턴
        
        if idx == n :
            idx = 1
            round += 1
        else :
            idx += 1
        
        first = 0
        last = word[-1]
        listUp.append(word)
    
    # words 리스트를 무사히 순회하면 [0, 0] 리턴
    return [0, 0]



#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))