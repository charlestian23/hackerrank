import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class RepeatedString 
{
	static long repeatedString(String s, long n) 
	{
        long repeated = n / s.length();
        long remainder = n % s.length();
        long count = s.replaceAll("[^a]", "").length() * repeated;
        for (int i = 0; i < remainder; i++)
        	if (s.charAt(i) == 'a')
        		count++;
        return count;
    }
	
	public static void main(String[] args)
	{
		System.out.println(repeatedString("aba", 10));
		System.out.println(repeatedString("a", 1000000000000L));
	}
}
