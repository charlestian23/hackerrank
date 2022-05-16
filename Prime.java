import java.io.*;
import java.util.*;

public class Prime {

	public static void main(String[] args) {
		int n = 2 * (int) Math.pow(10, 9);
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
	}
}
