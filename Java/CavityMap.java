// Unsolved, check for cavities bigger than 1x1

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class CavityMap {

    // Complete the cavityMap function below.
    static String[] cavityMap(String[] grid) {
        if (grid.length < 3 || grid[0].length() < 3)
            return grid;
        char[][] array = new char[grid.length][grid[0].length()];
        int g = 0;
        for (String s : grid) {
            array[g] = s.toCharArray();
            g++;
        }
        for (int i = 1; i < array.length - 1; i++)
            for (int j = 1; j < array[0].length - 1; j++)
            {
                int x = array[i][j];
                if (array[i - 1][j] < x && array[i + 1][j] < x && array[i][j - 1] < x && array[i][j + 1] < x)
                    array[i][j] = '!';
            }
        String[] answer = new String[grid.length];
        int counter = 0;
        for (char[] arr : array) {
            String s = "";
            for (char c : arr) {
                s += String.valueOf(c);
            }
            answer[counter] = s.replaceAll("!", "X");
            counter++;
        }
        System.out.println(Arrays.toString(answer));
        return answer;

    }

    public static void main(String[] args) {
        String[] s = {"333", "111", "191", "111", "333"};
        cavityMap(s);
    }

//    private static final Scanner scanner = new Scanner(System.in);

//    public static void main(String[] args) throws IOException {
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
//
//        int n = scanner.nextInt();
//        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
//
//        String[] grid = new String[n];
//
//        for (int i = 0; i < n; i++) {
//            String gridItem = scanner.nextLine();
//            grid[i] = gridItem;
//        }
//
//        String[] result = cavityMap(grid);
//
//        for (int i = 0; i < result.length; i++) {
//            bufferedWriter.write(result[i]);
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
}

