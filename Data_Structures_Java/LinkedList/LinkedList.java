package Data_Structures_Java.LinkedList;
//SLL
// While iterative traversal is more efficient due to recursion requiring a large call stack
// for bigger SLLs, both are used in the following class, in efforts to demonstrate knowledge of
// both.

public class LinkedList {
    Node head;

    LinkedList() {
        this.head = null;
    }

    public void add(int data) {
        if (isEmpty()) head = new Node(data, null);
        else add(head.next,data);
    }
    private void add(Node curr, int data) {
        if (curr.next == null) curr.next = new Node(data, null);
        else add(curr.next, data);
    }
    public void groupAdd(int[] arr) {
        for (int n: arr) add(n);
    }

    public boolean delete(int data) {
        if (head.data == data) {
            head = head.next;
            return true;
        }
        return delete(head.next, data);
    }
    private boolean delete(Node curr, int data) {
        if(curr == null || curr.next == null) return false;

        else if (curr.next.data == data) {
            curr.next = curr.next.next;
            return true;
        }
        
        return delete(curr.next, data);
    }

    public int[] toList() {
        if (isEmpty()) return new int[0];

        int size = getSize();
        int[] arr = new int[size];
        Node curr = head;

        for(int i = 0; i < size; i++) {
            arr[i] = curr.data;
            curr = curr.next;
        }
        return arr;
    }

    public int getSize() {
        if (isEmpty()) return 0;
        int size = 1;
        Node curr = head;

        while (curr != null) {
            size++;
            curr = curr.next;
        }

        return size;
    }

    public void print() {
        int[] ll = toList();

        for (int n: ll) System.out.print(n + "->");
    }

    public int pop() {
        if (head.next == null) {
            int popped = head.data;
            head = null;
            return popped;
        }
        Node curr = head;

        while(curr.next.next != null) {
            curr = curr.next;
        }

        int popped = curr.next.data;
        curr.next = null;

        return popped;
    }

    public boolean isEmpty() {
        if (head == null) return true;
        return false;
    }
}
