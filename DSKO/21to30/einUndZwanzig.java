package DSKO.21to30;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class einUndZwanzig {
    public int solution(String[] want, int[] number, String[] discount) {
        Map<String, Integer> di = new HashMap<>();
        for (int x = 0; x < number.length; x++) {
            di.put(want[x], x);
        }

        int[] li = new int[number.length];
        for (int y = 0; y < number.length; y++) {
            li[y] = number[y];
        }

        int answer = 0;

        for (int idx = 0; idx < discount.length - 9; idx++) {
            int[] tempLi = li.clone(); // 배열 복사
            for (int i = idx; i < idx + 10; i++) {
                try {
                    String tk = discount[i];
                    int tempLiIdx = di.get(tk);
                    if (tempLi[tempLiIdx] > 0) {
                        tempLi[tempLiIdx] -= 1;
                    }
                } catch (NullPointerException e) {
                    continue;
                }
            }
            int tempSum = Arrays.stream(tempLi).sum(); // 배열의 합을 계산하여 tempSum에 할당
            if (tempSum == 0) {
                answer++;
            }
        }
        return answer;
    }
}