import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class SockMerchant 
{
	// Complete the sockMerchant function below.
    static int sockMerchant(int n, int[] ar) {
        if (n == 1)
            return 0;
        Arrays.sort(ar);
        System.out.println(Arrays.toString(ar));
        int totalPairs = 0;
        int counter = 1;
        int previous = ar[0];
        for (int i = 1; i < n; i++)
        {
        	System.out.println("ARI" + ar[i]);
            if (ar[i] == previous)
                counter++;
            else
            {
            	System.out.println(previous + " " + counter);
                totalPairs += counter / 2;
                counter = 1;
                previous = ar[i];
            }
//            System.out.println(counter);
        }
        totalPairs += counter / 2;
        return totalPairs;
    }
    
    public static void main(String[] args)
    {
    	int[] x = {1, 1, 3, 1, 2, 1, 3, 3, 3, 3};
    	System.out.println("ANSWER" + sockMerchant(10, x));
    }
}
