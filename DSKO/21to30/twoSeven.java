package DSKO.21to30;

class twoSeven {
    // 프로그래머스 문제의 예시.
    public static void main(String[] args) {
        Solution sol = new Solution();
        int n = 8;
        int a = 4;
        int b = 7;
        System.out.println(sol.solution(n, a, b));
    }

    public int solution(int n, int a, int b) {
        int answer = 0; // 정답을 저장할 변수 answer

        while (true) {
            a = newNum(a);
            b = newNum(b);
            answer++;
            if (a == b) {
                break;
            }
        }

        return answer;
    }

    private int newNum(int x) {
        if (x % 2 == 0) {
            return x / 2;
        } else {
            return (x + 1) / 2;
        }
    }
}