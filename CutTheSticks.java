import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class CutTheSticks {

    // Complete the cutTheSticks function below.
    static int[] cutTheSticks(int[] arr) {
        ArrayList<Integer> array = new ArrayList<Integer>();
        ArrayList<Integer> sticks = new ArrayList<Integer>();
        Arrays.sort(arr);
        for (int i : arr)
            sticks.add(i);
        while (sticks.size() != 0)
        {
            int x = sticks.remove(0);
            if (x != 0)
            {
                array.add(sticks.size() + 1);
                for (int i = 0; i < sticks.size(); i++)
                    sticks.set(i, sticks.get(i) - x);
            }
        }
        int[] output = new int[array.size()];
        for (int i = output.length - 1; i >= 0; i--)
            output[i] = array.get(i);
        return output;
    }

    public static void main(String[] args)
    {
//        int[] arr = {5, 4, 4, 2, 2, 8};
        int[] arr = {1, 2, 3, 4, 3, 3, 2, 1};
        System.out.println(Arrays.toString(cutTheSticks(arr)));
    }


//    private static final Scanner scanner = new Scanner(System.in);

//    public static void main(String[] args) throws IOException {
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
//
//        int n = scanner.nextInt();
//        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
//
//        int[] arr = new int[n];
//
//        String[] arrItems = scanner.nextLine().split(" ");
//        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
//
//        for (int i = 0; i < n; i++) {
//            int arrItem = Integer.parseInt(arrItems[i]);
//            arr[i] = arrItem;
//        }
//
//        int[] result = cutTheSticks(arr);
//
//        for (int i = 0; i < result.length; i++) {
//            bufferedWriter.write(String.valueOf(result[i]));
//
//            if (i != result.length - 1) {
//                bufferedWriter.write("\n");
//            }
//        }
//
//        bufferedWriter.newLine();
//
//        bufferedWriter.close();
//
//        scanner.close();
//    }
}
