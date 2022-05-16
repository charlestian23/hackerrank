import java.io.*;
import java.util.*;

public class JavaSubarray {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int total = input.nextInt();
        int[] array = new int[total];
        for (int i = 0; i < total; i++)
            array[i] = input.nextInt();

        int counter = 0;
        for (int i = 0; i < total; i++) {
            int temp = 0;
            for (int j = i; j < total; j++) {
               temp += array[j];
               if (temp < 0)
                   counter++;
            }
        }

        System.out.println(counter);
    }
}