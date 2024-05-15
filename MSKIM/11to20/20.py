def solution(participant,completion):
    dict={}
    for p in participant:
        if p in dict:
            dict[p]+=1
        else:
            dict[p]=1

    for c in completion:
        dict[c]-=1

    for key in dict.keys():
        if dict[key]>0:
            return key