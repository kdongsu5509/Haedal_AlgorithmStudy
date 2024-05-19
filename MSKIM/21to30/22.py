#입력값 중에 고정된 값과 그렇지 않은 값이 있을떄
#고정된 값 == 딕셔너리의 키 -> 예외처리 줄일수있음


def solution(record):
    answer=[]
    uid={}
    for line in record:
        cmd=line.split(" ")
        if cmd[0] != "Leave":
            uid[cmd[1]]=cmd[2]
        for line in record:
            cmd=line.aplit(" ")
            if cmd[0]=="Enter":
                answer.append("%s님이 들어왔습니다." % uid[cmd[1]])
            elif cmd[0]=="Change":
                pass
            else:
                answer.append("%s님이 나갔습니다." % uid[cmd[1]])
        return answer