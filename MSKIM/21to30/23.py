def solution(genres,plays):
    answer=[]
    genres_dict={}
    play_dict={}

    for i in range(len(genres)):
        genre=genres[i]
        play=plays[i]
        #M.P) !!!
        # 키에 해당하는값이 없는 경우 반드시 초기화값을 명시해야 함 !!!
        if genre not in genres_dict:
            genres_dict[genre]=[]
            play_dict[genre]=0
        genres_dict[genre].append((i,play))
        play_dict[genre]+=play
        #재생횟수 많은순으로 장르 정렬
        sorted_generes=sorted(play_dict.items(),key=lambda x:x[1],reverse=True)

        #장르별 노래재생횟수 순으로 최대 2개 선정
        for genre, _ in sorted_generes:
            #각 장르에서 재생횟수 많은거 우선 -> 같으면 고유번호 낮은게 우선순위
            #재생횟수 많은게 우선순위니까 "-"붙임 / (reverse=True)이면 반대로부호
            sorted_songs=sorted(genres_dict[genre],key= lambda x: (-x[1],x[0]))
            answer.extend([idx for idx, _ in sorted_songs[:2]])
        return answer