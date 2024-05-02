public class siebzehn {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int ein = 0;
        int zwei = 0;
        for (String temp : goal) {
            if (ein < cards1.length && temp.equals(cards1[ein])) {
                ein++;
            } else if (zwei < cards2.length && temp.equals(cards2[zwei])) {
                zwei++;
            } else {
                answer = "No";
            }
        }
        return answer;
    }
}
