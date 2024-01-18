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
            if (curr.left != null) insertRecursive(curr.left, n);

            else curr.left = new Node(n, null, null);
        }
    }
}