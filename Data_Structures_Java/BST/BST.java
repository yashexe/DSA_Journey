package Data_Structures_Java.BST;

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
            if (curr.right != null) insertRecursive(curr.left, n);

            else curr.left = new Node(n, null, null);
        }
    }

    public int getHeight() {
        if (isEmpty()) return -1;

        Node curr = root;

        return getHeightRecursive(curr);
    }
    private int getHeightRecursive(Node curr) {
        if(curr.left != null){
            int left = getHeightRecursive(curr.left);
        } 
        else if(curr.right != null) {
            int right = getHeightRecursive(curr.right);
        }

        return Math.max(left, right);
    }
    public boolean isEmpty() {
        return root == null;
    }
}