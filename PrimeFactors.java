import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class PrimeFactors {

	/*
	 * Complete the primeCount function below.
	 */
	static int primeCount2(long n) {
		ArrayList<Long> numbers = new ArrayList<Long>();
		for (long i = 2; i <= n; i++)
			numbers.add(i);
		for (int i = 0; i < numbers.size(); i++) {
			long current = numbers.get(i);
			for (int j = i + 1; j < numbers.size(); j++)
				if (numbers.get(j) % current == 0) {
					numbers.remove(j);
					j--;
				}
		}
		int counter = 0;
		long total = 1;
		for (long l : numbers) {
			// System.out.println("l" + l + "\ttotal" + total + "\tcounter" + counter);
			if (total >= n)
				return counter;
			else {
				total *= l;
				counter++;
			}
		}
		return counter;
	}

	static int primeCount(long n) {
		long[] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 };
		int counter = 0;
		long total = 1;
		while (total < n && counter < primes.length) {
			total *= primes[counter];
			counter++;
		}
		if (total == n)
			return counter;
		else
			return counter - 1;
	}

	public static void main(String[] args) {
		System.out.println(primeCount(1L));
		System.out.println(primeCount(2L));
		System.out.println(primeCount(3L));
		System.out.println(primeCount(500L));
		System.out.println(primeCount(5000L));
		System.out.println(primeCount(10000000000L));
	}

}