import java.io.*;
import java.util.*;

public class MeanMedianMode {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int size = input.nextInt();
        int[] numbers = new int[size];
        for (int i = 0; i < size; i++)
        	numbers[i] = input.nextInt();
        Arrays.sort(numbers);
        double sum = 0;
        for (int i : numbers)
        	sum += i;
        System.out.println(sum / size);
        if (size % 2 == 0)
        	System.out.println((numbers[size / 2] + numbers[size / 2 - 1]) / 2.0);
        else
        	System.out.println(numbers[size / 2]);
        int bestPrevious = numbers[0];
        int bestCount = 1;
        int previous = numbers[0];
        int count = 1;
        for (int i = 1; i < size; i++)
        {
        	if (numbers[i] != previous)
        	{
        		if (count > bestCount)
        		{
        			bestCount = count;
        			bestPrevious = previous;
        		}
        		previous = numbers[i];
        		count = 0;
        	}
        	count++;
        }
        System.out.println(bestPrevious);
    }
}

