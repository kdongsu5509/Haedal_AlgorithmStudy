def polynomial_hash(str) :
    p = 31
    m = 1000000007
    hash_value = 0

    for char in str :
        hash_value = (hash_value * p + ord(char)) % m           # why???
    return hash_value

def solution(string_list, query_list) :
    # string_list에 있는 문자열들을 해싱해서 hash_list에 저장
    hash_list = [polynomial_hash(str) for str in string_list]

    result = []
    for query in query_list :
        query_hash = polynomial_hash(query)     # query_list에 있는 문자열(query)들을 해싱해서 query_hash에 저장
        if query_hash in hash_list :            
            result.append(True)                 # 해당 해싱값이 hash_list에 있으면 True 저장
        else :
            result.append(False)                # 해당 해싱값이 hash_list에 없으면 False 저장
    return result


#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]))