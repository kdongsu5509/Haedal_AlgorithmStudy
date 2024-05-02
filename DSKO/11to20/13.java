import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> st = new Stack<>();
        int answer = 0;
        int board_row = board.length;
        int board_col = board[0].length;
        
        for(int fixed_col : moves){
            for(int i = 0 ; i < board_row ; i++){
                int comp = board[i][fixed_col-1];
                if(comp != 0){
                    if(!st.empty() && st.peek() == comp){
                        st.pop();
                        answer += 2;
                        board[i][fixed_col-1] = 0;
                        break;
                    }else{
                        st.push(comp);
                        board[i][fixed_col-1] = 0;
                        break;
                    }
                }
            }
        }
        return answer;
    }
}

