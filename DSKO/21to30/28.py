def newNum(a):
    if a % 2 == 0:
        return a // 2
    else:
        return (a+1) // 2

def solution(n,a,b):
    #총 인원 수, a=참가자1의 번호 , b = 참가자 2의 번호
    cnt = 0
    
    while True:
        cnt += 1
        a = newNum(a)
        b = newNum(b)
        if a == b:
            break
        
    return cnt

#프로그래머스 문제 예시 테스트 케이스
print(solution(8, 4, 7))