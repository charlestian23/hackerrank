import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class MinimumSwaps {

    // Complete the minimumSwaps function below.

//    static int minimumSwaps(int[] arr) {
//        int swapCount = 0;
//        for (int i = 0; i < arr.length - 1; i++) {
//            int value = arr[i];
//            int index = i;
//            if (value != index + 1) {
//                for (int j = i; j < arr.length; j++)
//                    if (value > arr[j]) {
//                        value = arr[j];
//                        index = j;
//                    }
//                if (index != i) {
//                    arr[index] = arr[i];
//                    arr[i] = value;
//                    swapCount++;
//                }
//            }
//        }
//        return swapCount;
//    }

    static int minimumSwaps(int[] arr) {
        int swapCount = 0;
        for (int i = 0; i < arr.length - 1; i++) {
            int counter = i + 1;
            while (arr[i] != i + 1) {
                if (arr[counter] == i + 1) {
                    int temp = arr[counter];
                    arr[counter] = arr[i];
                    arr[i] = temp;
                    swapCount++;
                }
                counter++;
            }
        }
        return swapCount;
    }

//    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
//
//        int n = scanner.nextInt();
//        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
//
        int[] arr = {7, 1, 3, 2, 4, 5, 6};
//
//        String[] arrItems = scanner.nextLine().split(" ");
//        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
//
//        for (int i = 0; i < n; i++) {
//            int arrItem = Integer.parseInt(arrItems[i]);
//            arr[i] = arrItem;
//        }
//
        int res = minimumSwaps(arr);
        System.out.println(res);
//
//        bufferedWriter.write(String.valueOf(res));
//        bufferedWriter.newLine();
//
//        bufferedWriter.close();
//
//        scanner.close();
    }
}
