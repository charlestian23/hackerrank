import java.util.Arrays;
import java.util.Scanner;

public class Anagram {

    static boolean isAnagram(String a, String b) {
        String letters = "abcdefghijklmnopqrstuvwxyz";
        int[] count1 = new int[26];
        int[] count2 = new int[26];
        char[] x = a.toLowerCase().toCharArray();
        char[] y = b.toLowerCase().toCharArray();
        for (char c : x)
            count1[letters.indexOf(c)]++;
        for (char c : y)
            count2[letters.indexOf(c)]++;
//        System.out.println(Arrays.toString(count1));
//        System.out.println(Arrays.toString(count2));
        for (int i = 0; i < count1.length; i++)
            if (count1[i] != count2[i])
                return false;
        return true;
    }

    public static void main(String[] args) {
        String a = "anagramz";
        String b = "marganaz";
//        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
