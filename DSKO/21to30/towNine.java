import java.util.*;

public class towNine {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Map<String, String> parent = new HashMap<>();
        for (int i = 0; i < enroll.length; i++) {
            parent.put(enroll[i], referral[i]);
        }
        Map<String, Integer> total = new HashMap<>();
        for (int i = 0; i < seller.length; i++) {
            int r = amount[i] * 100;
            String person = seller[i];
            while (r > 0 && person != null) {
                int c = r / 10;
                r -= c;
                total.merge(person, r, Integer::sum);
                r = c;
                person = parent.get(person);
            }
        }
        int[] answer = new int[enroll.length];
        for (int i = 0; i < enroll.length; i++) {
            answer[i] = total.getOrDefault(enroll[i], 0);
        }
        return answer;
    }
}