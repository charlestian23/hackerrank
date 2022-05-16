import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class OrderEmail {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
//        HashMap<String, String> data = new HashMap<String, String>();
        ArrayList<String> names = new ArrayList<String>();
        for (int NItr = 0; NItr < N; NItr++) 
        {
            String[] firstNameEmailID = scanner.nextLine().split(" ");
            String firstName = firstNameEmailID[0];
            String emailID = firstNameEmailID[1];
            if (emailID.contains("@gmail.com"))
            	names.add(firstName);
//            	data.put(emailID, firstName);           
        }
        Collections.sort(names);
        for (String s : names)
        	System.out.println(s);
        scanner.close();
        
        
    }
}
