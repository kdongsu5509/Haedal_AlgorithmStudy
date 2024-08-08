def solution(phone_book) :
    # 접두어가 겹치는지 쉽게 확인하는 방법 : 정렬
    phone_book.sort()

    for i in range(len(phone_book)-1) :     # 두 개를 비교할 것이기 때문에 phone_book -1까지 비교
        if phone_book[i + 1].startswith(phone_book[i]) :        # startswith() : 앞의 변수가 매개변수로 시작하는지 분별
            return False                                        # 어떤 번호가 다른 번호의 접두어이면 False

    return True                                                 # 그렇지 않으면 True


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123", "456", "789"]))
# print(solution(["12", "123", "1235", "567", "88"]))