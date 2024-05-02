def solution(numbers):
    temp_set = set()
    for x in range(len(numbers)):
        for y in range(len(numbers)):
            if x!= y:
                temp_set.add(numbers[x] + numbers[y])
    return list(sorted(temp_set))