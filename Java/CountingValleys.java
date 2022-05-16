import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class CountingValleys 
{
	static int countingValleys(int n, String s) 
    {
        int total = 0;
        int previous = 0;
        int valleyCount = 0;
        for (int i = 0; i < n; i++)
        {
        	if (s.charAt(i) == 'U')
        		total++;
        	else if (s.charAt(i) == 'D')
        		total--;
        	else
        		break;
//        	System.out.println("PREVIOUS" + previous + " TOTAL" + total);
        	if (previous == -1 && total == 0)
        		valleyCount++;
        	previous = total;
        }
//        System.out.println("PREVIOUS" + previous + " TOTAL" + total);
        if (previous == -1 && total == 0)
    		valleyCount++;
        return valleyCount;
    }
	
	public static void main(String[] args)
	{
		System.out.println(countingValleys(8, "UDDDUDUU"));
	}
}
