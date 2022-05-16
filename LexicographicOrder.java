import java.util.Scanner;

public class LexicographicOrder {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'

        if (k >= s.length())
            return s + "\n" + s;

        smallest = s.substring(0, k);
        largest = s.substring(0, k);

        for (int i = 0; i <= s.length() - k; i++)
        {
            String substring = s.substring(i, i + k);
            if (substring.compareTo(smallest) < 0)
                smallest = substring;
            if (substring.compareTo(largest) > 0)
                largest = substring;
        }

        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}