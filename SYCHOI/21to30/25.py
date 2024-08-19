from itertools import combinations
from collections import Counter

def solution(orders, course) :
    answer = []

    for c in course :
        menu = []
        for order in orders :
            comb = combinations(
            sorted(order), c
            )
            menu += comb
        counter = Counter(menu)
        if (
            len(counter) != 0 and max(counter.values()) != 1
        ) :
            for m, cnt in counter.items() :
                if cnt == max(counter.values()) :
                    answer.append("".join(m))

    return  sorted(answer)


#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))