def solution(genres, plays) :
    genDict = {}
    plyDict = {}
    result = []

    for i in range(len(genres)) :
        genre = genres[i]
        play = plays[i]

        if genre not in genDict :
            genDict[genre] = []
            plyDict[genre] = 0
        genDict[genre].append((play, i))        # 해당 장르인 곡 각각의 재생수, 번호(play, i)를 item으로 입력
        plyDict[genre] += play                  # 해당 장르 곡의 총 재생수 

    # sorted_plyDict는 딕셔너리가 아닌 리스트 => items() 사용 불가
    sorted_plyDict = sorted(plyDict.items(), key=lambda x: x[1], reverse=True)      # plyDict 딕셔너리에서 value(x[1])를 기준으로 내림차순 정렬
    for genre in genDict :                                                          # genDict 딕셔너리에서 각 장르별로 순회
        genDict[genre].sort(key=lambda x: x[0], reverse=True)                       # genDict 딕셔너리의 특정 장르 내에서 play를 기준으로 내림차순 정렬
        # genDict도 sort() 함수로 인해 리스트화 됨

    for genre, play in sorted_plyDict :                 # 내림차순 정렬된 plyDict 리스트를 차례대로 순회
        for i in range(2) :                             # 각 장르별로 최대 2곡까지 수록
            if genDict[genre][i] :                      # 해당 장르에 곡이 있으면
                result.append(genDict[genre][i][1])


    return result


#TEST 코드입니다. 주석을 풀어서 확인해보세요
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))