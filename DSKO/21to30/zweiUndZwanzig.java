package DSKO.21to30;

import java.util.*;

public class zweiUndZwanzig {
    public String[] solution(String[] record) {
        List<String> answer = new ArrayList<>();
        Map<String, String> namespace = new HashMap<>();
        Map<String, String> printer = new HashMap<>();

        printer.put("Enter", "님이 들어왔습니다.");
        printer.put("Leave", "님이 나갔습니다.");

        for (String r : record) {
            // System.out.println(r);
            String[] rr = r.split(" ");
            // for(String x : rr){
            // System.out.println(x);
            // }
            if (rr[0].equals("Enter") || rr[0].equals("Change")) {
                namespace.put(rr[1], rr[2]);
            }
        }

        for (String r : record) {
            String[] rr = r.split(" ");
            if (!rr[0].equals("Change")) {
                answer.add(namespace.get(rr[1]) + printer.get(rr[0]));
            }
        }
        String[] answer2 = toArr(answer);
        return answer2;
    }

    private String[] toArr(List<String> temp) {
        int s = temp.size();

        String[] re = new String[s];
        for (int idx = 0; idx < s; idx++) {
            re[idx] = temp.get(idx);
        }

        return re;
    }
}
