def solution(record):
    temp_set = set()
    for x in record:
        s = list(map(str, x.split(" ")))
        temp_set.add(s[1])
        
    temp_li = list(temp_set)
    
    hash_dict_nick = dict()
    idx = 0
    for x in temp_li:
        hash_dict_nick[x] = ""
    
    # print(hash_dict_nick)
    
    
    result = []
    for order in record:
        t = list(map(str, order.split(" ")))
        # print(t)
        command = t[0]
        user_id = t[1]
        try:
            nickname = t[2]
        except:
            nickname = " "
        # nickname = t[2]
        # print(command)
        # print(user_id)
        # print(nickname)
        if(command == "Enter"):
            hash_dict_nick[user_id] = nickname
            result.append([user_id, 0])
        elif(command == "Leave"):
            result.append([user_id, 1])
        elif(command == "Change"):
        # hash_dict_nick[user_id] = nickname
            hash_dict_nick[user_id] = nickname
            
    answer = []
    for r in result:
        if r[1] == 1:
            answer.append(hash_dict_nick[r[0]] + "님이 나갔습니다.")
        else:
            answer.append(hash_dict_nick[r[0]] + "님이 들어왔습니다.")
            
    
    return answer
