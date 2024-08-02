def solution(record) :
    result = []
    dict = {}
    for data in record :
        state = data.split()[0]
        if state == "Enter" or state == "Change":   # Enter과 Change 상태에서 닉네임 변경
            id = data.split()[1]
            name = data.split()[2]
            dict[id] = name                         # 유저 ID에 따라 닉네임 변경
    
    # cmd = data.split() => cmd[0], cmd[1], cmd[2]로 사용 가능

    for data in record :
        state = data.split()[0]
        id = data.split()[1]

        if data.split()[0] == "Enter" :
            # print(dict[id], "님이 들어왔습니다.")
            result.append("%s님이 들어왔습니다." %dict[id])
        elif data.split()[0] == "Leave" :
            # print(dict[id], "님이 나갔습니다.")
            result.append("%s님이 나갔습니다." %dict[id])
    
    return result

#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))