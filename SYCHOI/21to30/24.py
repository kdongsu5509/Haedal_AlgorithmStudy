def solution(id_list, report, k) :
    reported_user = {}
    count = {}

    for r in report :
        user_id, reported_id = r.split()
        if reported_id not in reported_user :
            reported_user[reported_id] = set()
        reported_user[reported_id].add(user_id)

    for reported_id, user_id_lst in reported_user.items() :
        if len(user_id_lst) >= k :
            for uid in user_id_lst :
                if uid not in count :
                    count[uid] = 1
                else :
                    count[uid] += 1

    answer = []
    for i in range(len(id_list)) :
        if id_list[i] not in count :
            answer.append(0)
        else :
            answer.append(count[id_list[i]])

    return answer


#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))










# def solution(id_list, report, k) :
#     id_dict = dict.fromkeys(id_list, 0)     # 해당 아이디가 신고당한 횟수 기록
#     report_dict = {}                        # 신고자 - 피신고자(리스트 형태) 기록
#     mail_dict = dict.fromkeys(id_list, 0)   # 신고자가 받을 메일 개수 기록

#     for names in report :
#         idx = names.split()

#         if report_dict.get(idx[0]) == None :
#             report_dict[idx[0]] = list()

#         if idx[1] not in report_dict[idx[0]] :
#             report_dict[idx[0]].append(idx[1])
#             id_dict[idx[1]] += 1


#     rpt = 0; rpte = 0

#     while(1) :
#         name = id_list[rpt]

#         if report_dict.get(id_dict[name]) == None :
#             rpt += 1
#             continue
#         elif report_dict[id_dict[name]][rpte] >= 2 :
#             mail_dict[rpt] += 1

#         if report_dict[id_dict[name]][rpte+1] == None :
#             rpt = 0
#             rpte = 0
#         else :
#             rpte += 1

#     result = list(mail_dict.values())

#     print(id_dict)
#     print(report_dict)

#     return result


# #TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))