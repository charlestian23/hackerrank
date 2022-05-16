import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class PrimeCount {
	static int primeCount(long n) {
		/*
		 * Write your code here.
		 */
		if (n == 1)
			return 0;
		ArrayList<Long> primeNumbers = new ArrayList<Long>();
		for (int i = 2; i <= n; i++)
		{
			boolean check = true;
			for (int j = 0; j < primeNumbers.size(); j++)
			{
//				System.out.println(primeNumbers.get(j));
				if (i % primeNumbers.get(j) == 0)
				{
					check = false;
					break;
				}
			}
//			System.out.println(check);
			if (check)
				primeNumbers.add((long) i);
		}
		return primeNumbers.size();
	}
	
	public static void main(String[] args)
	{
//		System.out.println(primeCount(1L));
//		System.out.println(primeCount(2L));
//		System.out.println(primeCount(3L));
//		System.out.println(primeCount(500L));
//		System.out.println(primeCount(5000L));
//		System.out.println(primeCount(10000000000L));
	}
	
//	1
//	2
//	3
//	500
//	5000
//	10000000000
}
