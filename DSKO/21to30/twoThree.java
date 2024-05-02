package DSKO.21to30;

import java.util.*;

public class twoThree {
    public static int[] solution(String[] genres, int[] plays) {
        List<Integer> answerList = new ArrayList<>();
        Map<String, List<int[]>> genresMap = new HashMap<>();
        Map<String, Integer> playMap = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            if (!genresMap.containsKey(genre)) {
                genresMap.put(genre, new ArrayList<>());
                playMap.put(genre, 0);
            }
            genresMap.get(genre).add(new int[] { i, play });
            playMap.put(genre, playMap.get(genre) + play);
        }

        List<Map.Entry<String, Integer>> sortedGenres = new ArrayList<>(playMap.entrySet());
        Collections.sort(sortedGenres, (a, b) -> b.getValue().compareTo(a.getValue()));

        for (Map.Entry<String, Integer> entry : sortedGenres) {
            List<int[]> songs = genresMap.get(entry.getKey());
            songs.sort((a, b) -> {
                if (a[1] != b[1])
                    return Integer.compare(b[1], a[1]);
                return 0;
            });
            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                answerList.add(songs.get(i)[0]);
            }
        }

        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}
