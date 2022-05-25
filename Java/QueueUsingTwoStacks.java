import java.util.Stack;
import java.util.Scanner;

public class QueueUsingTwoStacks
{
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public QueueUsingTwoStacks()
    {
        stack1 = new Stack<Integer>(); // dequeue stack
        stack2 = new Stack<Integer>(); // enqueue stack
    }

    public void enqueue(int value)
    {
        stack2.push(value);
    }

    public int dequeue()
    {
        if (stack1.isEmpty())
            while (!stack2.isEmpty())
                stack1.push(stack2.pop());
        return stack1.pop();
    }

    public void print()
    {
        if (stack1.isEmpty())
            while (!stack2.isEmpty())
                stack1.push(stack2.pop());
        System.out.println(stack1.peek());
    }

    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        QueueUsingTwoStacks queue = new QueueUsingTwoStacks();
        int queries = scanner.nextInt();
        for (int i = 0; i < queries; i++)
        {
            int query = scanner.nextInt();
            if (query == 1)
            {
                int value = scanner.nextInt();
                queue.enqueue(value);
            }
            else if (query == 2)
                queue.dequeue();
            else if (query == 3)
                queue.print();
        }
    }
}