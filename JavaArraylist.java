import java.io.*;
import java.util.*;

public class JavaArraylist {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int size = input.nextInt();
        ArrayList<Integer>[] array = new ArrayList[size];
        for (int i = 0; i < size; i++)
        {
            ArrayList<Integer> list = new ArrayList<Integer>();
            int x = input.nextInt();
            for (int j = 0; j < x; j++)
                list.add(input.nextInt());
            array[i] = list;
        }
        int inputs = input.nextInt();
        for (int i = 0; i < inputs; i++)
        {
            int line = input.nextInt();
//            System.out.println(line);
            int position = input.nextInt();
//            System.out.println(position);
            if (line < 1 || line > array.length)
                System.out.println("ERROR!");
            else
            {
                ArrayList<Integer> a = array[line - 1];
                if (position < 1 || position > a.size())
                    System.out.println("ERROR!");
                else
                    System.out.println(a.get(position - 1));
            }
        }
    }
}