import java.util.Stack;

class Solution {
    public int solution(String s) {
        int cnt = 0;

        // 문자열을 회전하면서 유효한 괄호인지 확인
        for (int i = 0; i < s.length(); i++) {
            String rotated = rotate(s, i);
            if (validity(rotated)) {
                cnt++;
            }
        }

        return cnt;
    }

    // 문자열을 회전시키는 메서드
    private String rotate(String s, int offset) {
        return s.substring(offset) + s.substring(0, offset);
    }

    // 문자열에 대한 유효성을 검사하는 메서드
    private boolean validity(String temp) {
        Stack<Character> stack = new Stack<>();
        for (char c : temp.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' && !stack.isEmpty() && stack.peek() == '(') {
                stack.pop();
            } else if (c == '}' && !stack.isEmpty() && stack.peek() == '{') {
                stack.pop();
            } else if (c == ']' && !stack.isEmpty() && stack.peek() == '[') {
                stack.pop();
            } else {
                return false; // 올바른 괄호가 아닌 경우
            }
        }
        return stack.isEmpty(); // 스택이 비어있어야 모든 괄호가 올바르게 매칭됨
    }
}
