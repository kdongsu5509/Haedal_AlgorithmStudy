class Node {
    int val;
    Node left, right;

    Node(int key) {
        val = key;
        left = right = null;
    }
}

class BST {
    Node root;

    BST() {
        root = null;
    }

    void insert(int key) {
        root = insertRec(root, key);
    }

    Node insertRec(Node root, int key) {
        if (root == null) {
            root = new Node(key);
            return root;
        }

        if (key < root.val) {
            root.left = insertRec(root.left, key);
        } else if (key > root.val) {
            root.right = insertRec(root.right, key);
        }

        return root;
    }

    boolean search(int key) {
        return searchRec(root, key);
    }

    boolean searchRec(Node root, int key) {
        if (root == null) {
            return false;
        }

        if (root.val == key) {
            return true;
        }

        if (key < root.val) {
            return searchRec(root.left, key);
        }

        return searchRec(root.right, key);
    }
}

public class twoSeven {
    public static void main(String[] args) {
        BST bst = new BST();

        int[] lst = { 1, 3, 5, 7, 9 };
        int[] searchList = { 2, 4, 6, 8, 10 };
        for (int i : lst) {
            bst.insert(i);
        }

        System.out.print("Test case 1: ");
        for (int i : searchList) {
            System.out.print(bst.search(i) + " ");
        }
        System.out.println();

        int[] lst2 = { 5, 3, 8, 4, 2, 1, 7, 10 };
        int[] searchList2 = { 1, 2, 5, 6 };
        BST bst2 = new BST();
        for (int i : lst2) {
            bst2.insert(i);
        }

        System.out.print("Test case 2: ");
        for (int i : searchList2) {
            System.out.print(bst2.search(i) + " ");
        }
    }
}
