import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class AppleAndOrange {

    // Complete the countApplesAndOranges function below.
    static void countApplesAndOranges(int s, int t, int a, int b, int[] apples, int[] oranges) {
        int appleCounter = 0;
        for (int i : apples)
            if (a + i >= s && a + i <= t) {
//                System.out.println(i);
                appleCounter++;
            }
        int orangeCounter = 0;
        for (int i : oranges)
            if (b + i >= s && b + i <= t) {
                orangeCounter++;
//                System.out.println(i);
            }
        System.out.println(appleCounter);
        System.out.println(orangeCounter);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args)
    {
        int a = -8;
        int s = -6;
        int t = -4;
        int b = -2;
        int[] apples = {0, 1, -2, -3, 2, 3, 4, 10};
        int[] oranges = {0, 1, -2, -3, 2, 3, 4, 10};
        countApplesAndOranges(s, t, a, b, apples, oranges);
    }

//    public static void main(String[] args) {
//        String[] st = scanner.nextLine().split(" ");
//
//        int s = Integer.parseInt(st[0]);
//
//        int t = Integer.parseInt(st[1]);
//
//        String[] ab = scanner.nextLine().split(" ");
//
//        int a = Integer.parseInt(ab[0]);
//
//        int b = Integer.parseInt(ab[1]);
//
//        String[] mn = scanner.nextLine().split(" ");
//
//        int m = Integer.parseInt(mn[0]);
//
//        int n = Integer.parseInt(mn[1]);
//
//        int[] apples = new int[m];
//
//        String[] applesItems = scanner.nextLine().split(" ");
//        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
//
//        for (int i = 0; i < m; i++) {
//            int applesItem = Integer.parseInt(applesItems[i]);
//            apples[i] = applesItem;
//        }
//
//        int[] oranges = new int[n];
//
//        String[] orangesItems = scanner.nextLine().split(" ");
//        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
//
//        for (int i = 0; i < n; i++) {
//            int orangesItem = Integer.parseInt(orangesItems[i]);
//            oranges[i] = orangesItem;
//        }
//
//        countApplesAndOranges(s, t, a, b, apples, oranges);
//
//        scanner.close();
//    }
}
