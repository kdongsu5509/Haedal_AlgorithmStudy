from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()

    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = (remain + speeds[i] - 1) // speeds[i]
        days.append(day)
        
    while days:
        current_day = days.popleft()  
        count = 1
        while days and days[0] <= current_day:
            count += 1
            days.popleft()
        answer.append(count)

    return answer