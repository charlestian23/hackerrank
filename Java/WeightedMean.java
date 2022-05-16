import java.io.*;
import java.text.DecimalFormat;
import java.util.*;

public class WeightedMean 
{
	public static void main(String[] args)
	{
		DecimalFormat df = new DecimalFormat("##0.0");
		Scanner input = new Scanner(System.in);
		int count = input.nextInt();
		int[] numbers = new int[count];
		int[] weight = new int[count];
		for (int i = 0; i < count; i++)
			numbers[i] = input.nextInt();
		double weightTotal = 0;
		for (int i = 0; i < count; i++)
		{
			weight[i] = input.nextInt();
			weightTotal += weight[i];
		}
		double total = 0;
		for (int i = 0; i < count; i++)
			total += numbers[i] * weight[i];
		System.out.println(df.format(total / weightTotal));
	}
}
