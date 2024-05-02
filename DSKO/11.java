import java.util.Stack;

class Solution {
    public int solution(String s) {
        Stack st = new Stack();
        char[] chArr = s.toCharArray();
        for (char x : chArr) {
            if (st.empty()) {
                st.push(x);
            } else if (!st.empty() && (char) st.peek() != x) {
                st.push(x);
            } else if (!st.empty() && (char) st.peek() == x) {
                st.pop();
            }
        }
        int answer = (st.size() == 0) ? 1 : 0;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        // System.out.println("Hello Java");

        return answer;
    }
}