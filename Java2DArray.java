import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Java2DArray {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int maxSum = -9 * 7;
        for (int x = 0 ; x < 4; x++)
            for (int y = 0; y < 4; y++)
            {
//                System.out.println(arr[x][y]);
                int sum = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 1] + arr[x + 2][y]
                        + arr[x + 2][y + 1] + arr[x + 2][y + 2];
                System.out.println(sum);
                if (sum > maxSum)
                    maxSum = sum;
            }
        System.out.println(maxSum);
        scanner.close();
    }
}
