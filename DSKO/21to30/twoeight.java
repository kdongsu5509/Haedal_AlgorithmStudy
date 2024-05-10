public class twoEight {
    public int solution(int n, int a, int b) {
        int cnt = 0;
        while (true) {
            a = (int) Math.ceil((double) a / 2);
            b = (int) Math.ceil((double) b / 2);

            cnt++;
            if (a == b) {
                return cnt;
            }
        }
    }
}