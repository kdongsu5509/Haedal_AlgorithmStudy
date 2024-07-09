public class twoSix {
    public static void main(String[] args) {
        int[] list = { 1, 2, 3, 4, 5, 6, 7 };
        String[] result = solution(list);
        for (String str : result) {
            System.out.println(str);
        }
    }

    public static String[] solution(int[] list) {
        String preOrder = preorder(list, 0);
        String inOrder = inorder(list, 0);
        String postOrder = postorder(list, 0);

        String[] result = new String[] { preOrder.trim(), inOrder.trim(), postOrder.trim() };

        return result;
    }

    private static String preorder(int[] list, int index) {
        StringBuilder sb = new StringBuilder();
        if (index < list.length) {
            sb.append(list[index]).append(" ");
            sb.append(preorder(list, 2 * index + 1));
            sb.append(preorder(list, 2 * index + 2));
        }
        return sb.toString();
    }

    private static String inorder(int[] list, int index) {
        StringBuilder sb = new StringBuilder();
        if (index < list.length) {
            sb.append(inorder(list, 2 * index + 1));
            sb.append(list[index]).append(" ");
            sb.append(inorder(list, 2 * index + 2));
        }
        return sb.toString();
    }

    private static String postorder(int[] list, int index) {
        StringBuilder sb = new StringBuilder();
        if (index < list.length) {
            sb.append(postorder(list, 2 * index + 1));
            sb.append(postorder(list, 2 * index + 2));
            sb.append(list[index]).append(" ");
        }
        return sb.toString();
    }
}
