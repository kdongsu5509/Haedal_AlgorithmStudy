import math

def solution(enroll, referral, seller, amount) :
    dict = {}
    earn = {}
    for i in range(len(enroll)) : 
        dict[enroll[i]] = referral[i]
        earn[enroll[i]] = 0

    for i in range(len(seller)) :
        name = seller[i]
        money = amount[i] * 100     # 칫솔 개당 100원

        while name != "-" :
            if earn[name] == 0 :
                earn[name] = money * 0.9
            else : 
                earn[name] += money * 0.9
            money = money * 0.1         # referral이 enroll한테 넘겨받은 돈(10%)
            if money < 1 :
                earn[name] += money     # 10%를 계산한 금액이 1원 미만이면 이득을 분배하지 않고 자신이 모두 가짐
            name = dict[name]           # referral을 name에 초기화

    result = []
    for value in earn.values() :
        result.append(round(value))
    return result



    
#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))