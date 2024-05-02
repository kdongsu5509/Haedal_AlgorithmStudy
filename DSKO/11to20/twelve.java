import java.util.Stack;

class twelve {
    public int[] solution(int[] prices) {
        Stack<int[]> st = new Stack<>();
        int[] time = new int[prices.length];

        int idx = 0;
        for (; idx < prices.length; idx++) {
            if (st.empty() || st.peek()[0] <= prices[idx]) {
                int[] temp = new int[2];
                temp[0] = prices[idx];
                temp[1] = idx;
                st.push(temp);
            } else {
                while (!st.empty() && st.peek()[0] > prices[idx]) {
                    int[] t = st.pop();
                    int out_idx = t[1];
                    time[out_idx] = idx - out_idx;
                }
                int[] temp = new int[2];
                temp[0] = prices[idx];
                temp[1] = idx;
                st.push(temp);
            }
        }
        // 나머지 스택 처리
        while (!st.empty()) {
            int[] t = st.pop();
            int out_idx = t[1];
            time[out_idx] = idx - out_idx - 1;
        }
        return time;
    }
}
