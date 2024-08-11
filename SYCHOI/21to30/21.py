def solution(want, number, discount) :
    dic = {}
    
    # 정현이가 원하는 제품과 개수를 dictionary에 저장
    for i in range(len(want)) :
        dic[want[i]] = number[i]

    # 할인 상품과 원하는 제품 비교
    cnt = 0         # 원하는 제품을 모두 할인받을 수 있는 회원 등록 날짜 수
    for j in range(len(discount) - 9) :     # 10일 순회할 수 있을 만큼만 discount 순회
        tenDays = {}

        for k in range(j, j + 10) :     # 특정 날짜(k)부터 10일간 discount 물품 순회
            if discount[k] in dic :     # 할인 품목이 정현이가 원하는 제품 목록에 있으면
                tenDays[discount[k]] = tenDays.get(discount[k], 0) + 1      # 10일동안 할인받는 물품들의 개수를 tenDays 딕셔너리에 저장
                                                                            # tenDays에 이미 있으면 해당 값(value) + 1, 없으면 기본값(default value) + 1
            if tenDays == dic :
                cnt += 1            # 10일 연속으로 원하는 제품을 개수만큼 할인받을 수 있다면 cnt++
                break               # 책과 다름. 조금 수정함..
        

    return cnt

        



#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))