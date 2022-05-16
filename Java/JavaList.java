import java.io.*;
import java.util.*;

public class JavaList {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int length = input.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < length; i++)
            list.add(input.nextInt());
        int queries = input.nextInt();
        for (int i = 0; i < queries; i++)
        {
            input.nextLine();
            String str = input.nextLine();
            if (str.equals("Insert"))
            {
                int position = input.nextInt();
                list.add(position, input.nextInt());
            }
            else
                list.remove(input.nextInt());
        }
        for (int i : list)
            System.out.print(i + " ");
    }
}