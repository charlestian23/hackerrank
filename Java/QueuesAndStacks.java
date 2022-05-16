import java.io.*;
import java.util.*;

public class QueuesAndStacks {
    // Write your code here.
	private Queue<Character> q;
	private Stack<Character> c;
	
	public QueuesAndStacks()
	{
		q = new LinkedList<Character>();
		c = new Stack<Character>();
	}
	
	void pushCharacter(char x)
	{
		c.push(x);
	}
	
	char popCharacter()
	{
		return c.pop();
	}
	
	void enqueueCharacter(char x)
	{
		q.add(x);
	}
	
	char dequeueCharacter()
	{
		return q.remove();
	}

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        scan.close();

        // Convert input String to an array of characters:
        char[] s = input.toCharArray();

        // Create a Solution object:
        QueuesAndStacks p = new QueuesAndStacks();

        // Enqueue/Push all chars to their respective data structures:
        for (char c : s) {
            p.pushCharacter(c);
            p.enqueueCharacter(c);
        }

        // Pop/Dequeue the chars at the head of both data structures and compare them:
        boolean isPalindrome = true;
        for (int i = 0; i < s.length/2; i++) {
            if (p.popCharacter() != p.dequeueCharacter()) {
                isPalindrome = false;                
                break;
            }
        }

        //Finally, print whether string s is palindrome or not.
        System.out.println( "The word, " + input + ", is " 
                           + ( (!isPalindrome) ? "not a palindrome." : "a palindrome." ) );
    }
}