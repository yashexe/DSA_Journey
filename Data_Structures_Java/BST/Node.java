package Data_Structures_Java.BST;

public class Node {
    int data;
    Node left;
    Node right;

    Node(int n, Node l, Node r) {
        this.data = n;
        this.left = l;
        this.right = r;
    }
}