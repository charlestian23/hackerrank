import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class TimeConversion {

    /*
     * Complete the timeConversion function below.
     */
    static String timeConversion(String s) {
        /*
         * Write your code here.
         */
        if (s.substring(0, 2).equals("12"))
        {
            String[] array = s.split(":");
            int newTime = Integer.parseInt(array[0]) - 12;
            if (newTime == 0)
                s = "00" + s.substring(2);
            else
                s = newTime + s.substring(2);
            System.out.println(s);
        }
        if (s.substring(s.length() - 2).equals("AM"))
            return s.substring(0, s.length() - 2);
        else
        {
            String[] array = s.split(":");
            int newTime = Integer.parseInt(array[0]) + 12;
            return newTime + s.substring(2, s.length() - 2);
        }
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scan.nextLine();

        String result = timeConversion(s);

        bw.write(result);
        bw.newLine();

        bw.close();
    }
}
