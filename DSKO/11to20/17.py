from collections import deque

def solution(cards1, cards2, goal):
    ein = deque(cards1)
    zwei = deque(cards2)
    
    for word in goal:
        if(len(ein) != 0 and ein[0] == word):
            ein.popleft()
        elif(len(zwei) != 0 and zwei[0] == word):
            zwei.popleft()
        else:
            return "No"

    
    return "Yes"