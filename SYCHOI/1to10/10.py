def solution(s) :
    stack1 = []     # ()
    stack2 = []     # {}
    stack3 = []     # []
    
    sList = list(s)
    cnt = 0

    for i in range(len(s)) :            # 문자열 s는 s의 길이만큼 회전함

        for x in sList :                # 문자열 순회
            if x == '(' :
                stack1.append(x)
            elif x == '{' :
                stack2.append(x)
            elif x == '[' :
                stack3.append(x)
                
            elif x == ')' :
                if not stack1 :
                    stack1.append(x)     # cnt하지 않기 위해 넣고 break
                    break
                else :
                    stack1.pop()
            elif x == '}' :
                if not stack2 :
                    stack2.append(x)
                    break
                else :
                    stack2.pop()
            elif x == ']' :
                if not stack3 :
                    stack3.append(x)
                    break
                else :
                    stack3.pop()

        if not stack1 and not stack2 and not stack3 :
            cnt += 1

        idx = sList[0]
        sList.remove(sList[0])
        sList.append(idx)
        stack1.clear(); stack2.clear(); stack3.clear()

    return cnt


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution("[](){}"))
# print(solution("}]()[{"))
# print(solution("[)(]"))
# print(solution("}}}"))