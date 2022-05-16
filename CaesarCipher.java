import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class CaesarCipher {

    // Complete the caesarCipher function below.
    static String caesarCipher(String s, int k) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        char[] array = s.toCharArray();
        for (int i = 0; i < s.length(); i++)
            if (alphabet.indexOf(array[i]) != -1 || alphabet.toUpperCase().indexOf(array[i]) != -1)
            {
                int max = 0;
                if (array[i] >= 65 && array[i] <= 90)
                    max = 90;
                else if (array[i] >= 97 && array[i] <= 122)
                    max = 122;
                int temp = array[i] + k;
                while (temp > max)
                    temp -= 26;
                array[i] = (char) temp;
            }
        String str = "";
        for (char c : array)
            str += c;
        return str;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String s = scanner.nextLine();

        int k = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String result = caesarCipher(s, k);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
