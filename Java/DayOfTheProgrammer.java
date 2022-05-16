import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class DayOfTheProgrammer {

    static final int[] regYear = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    static final int[] leapYear = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    static final int[] year1918 = {0, 31, 15, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // Complete the dayOfProgrammer function below.
    static String dayOfProgrammer(int year) {
        DecimalFormat df = new DecimalFormat("00");
        int array[] = new int[0];
        if (year >= 1919 && ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0))
            array = leapYear;
        else if (year < 1917 && year % 4 == 0)
            array = leapYear;
        else if (year == 1918)
            array = year1918;
        else
            array = regYear;
        int counter = 0;
        int days = 256;
        while (days > array[counter] && counter <= 12)
        {
            counter++;
            days -= array[counter];
        }
        return days + "." + df.format(counter + 1) + "." + year;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int year = Integer.parseInt(bufferedReader.readLine().trim());

        String result = dayOfProgrammer(year);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
