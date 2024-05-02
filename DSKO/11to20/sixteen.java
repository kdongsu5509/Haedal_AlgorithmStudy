import java.util.*;

public class sixteen {
    public static List<Integer> solution(int[] progresses, int[] speeds) {
        Deque<Integer> pr = new LinkedList<>();
        Deque<Integer> sp = new LinkedList<>();
        for (int progress : progresses) {
            pr.add(progress);
        }
        for (int speed : speeds) {
            sp.add(speed);
        }
        List<Integer> answer = new ArrayList<>();
        while (!pr.isEmpty()) {
            int cnt = 0;
            for (int i = 0; i < pr.size(); i++) {
                int progress = pr.poll();
                int speed = sp.poll();
                progress += speed;
                pr.add(progress);
                sp.add(speed);
            }
            if (!pr.isEmpty() && pr.peek() >= 100) {
                while (!pr.isEmpty() && pr.peek() >= 100) {
                    cnt++;
                    pr.poll();
                    sp.poll();
                }
                answer.add(cnt);
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] progresses = { 93, 30, 55 };
        int[] speeds = { 1, 30, 5 };
        List<Integer> result = solution(progresses, speeds);
        System.out.println(result);
    }
}
