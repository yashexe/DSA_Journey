package Data_Structures_Java.BST;

import java.lang.Math;

public class BST {
    private Node root;

    public BST(Node root){
        root = null;
    }

    public void insert(int n) {
        if(root != null) {
            Node curr = root;
            insertRecursive(curr, n);
        }

        else root = new Node(n, null, null);
    }

    private void insertRecursive(Node curr, int n) {
        if(n > curr.data) {
            if (curr.right != null) insertRecursive(curr.right, n);

            else curr.right = new Node(n, null, null);
        }
        else if (n < curr.data) {
            if (curr.left != null) insertRecursive(curr.left, n);

            else curr.left = new Node(n, null, null);
        }
    }

    public void insertMultiple(int[] arr) {
        for (int n: arr) insert(n);
    }

    public int getHeight() {
        if (isEmpty()) return -1;
        else if (root.left == null && root.right == null) return 0;

        Node curr = root;

        return getHeightRecursive(curr);
    }

    private int getHeightRecursive(Node curr) {
        int left = 0;
        int right = 0;

        if(curr.left != null){
            left = getHeightRecursive(curr.left);
        } 
        else if(curr.right != null) {
            right = getHeightRecursive(curr.right);
        }

        return Math.max(left, right) + 1;
    }

    public boolean isEmpty() {
        return root == null;
    }

    public Node search(Node root, int data) {
        if(root == null || root.data == data) return null;

        if(data > root.data) return search(root.right, data);

        else return search(root.left, data);
    }

    public void printPreorder(Node root) {
        if (root != null) {
            System.out.println(root.data);
            printPreorder(root.left);
            printPreorder(root.right);
        }   
    }
    public void printInorder(Node root) {
        if (root != null) {
            printInorder(root.left);
            System.out.println(root.data);
            printInorder(root.right);
        }
    }
    public void printPostorder(Node root) {
        if (root != null) {
            printPostorder(root.left);
            printPostorder(root.right);
            System.out.println(root.data);
        }
    }
}