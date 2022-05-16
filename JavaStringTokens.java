import java.io.*;
import java.util.*;

public class JavaStringTokens {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        s = s.trim();
        String token = "[ !,?._'@\\s]+";
        if (s.length() == 0)
            System.out.println(0);
        else {
            String[] array = s.split(token);
            System.out.println(array.length);
            for (String x : array)
                System.out.println(x);
        }
        scan.close();
    }
}