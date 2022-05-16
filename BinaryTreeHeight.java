import java.util.*;
import java.io.*;

class Node {
    public Node next;
    Node left;
    Node right;
    int data;

    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class BinaryTreeHeight {

    /*
    class Node 
        int data;
        Node left;
        Node right;
    */
    public static int height(Node root) {
        if (root == null)
            return -1;
        int left = height(root.left) + 1;
        int right = height(root.right) + 1;
        if (left > right)
            return left;
        return right;
    }

    public static Node insert(Node root, int data) {
        if(root == null) {
            return new Node(data);
        } else {
            Node cur;
            if(data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        Node root = null;
        while(t-- > 0) {
            int data = scan.nextInt();
            root = insert(root, data);
        }
        scan.close();
        int height = height(root);
        System.out.println(height);
    }
}