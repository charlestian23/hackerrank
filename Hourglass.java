import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Hourglass 
{
	static int hourglassSum(int[][] arr) 
	{
		int maxSum = Integer.MIN_VALUE;
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++)
			{
//				System.out.println(arr[x + 1][y + 2]);
				int sum = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 1] + arr[x + 2][y] + arr[x + 2][y + 1] + arr[x + 2][y + 2];
//				System.out.println(sum);
				if (sum > maxSum)
					maxSum = sum;
			}
		return maxSum;
    }
	
	public static void main(String[] args)
	{
		int[][] arr = {	{1, 1, 1, 0, 0, 0},
						{0, 1, 0, 0, 0, 0},
						{1, 1, 1, 0, 0, 0},
						{0, 0, 2, 4, 4, 0},
						{0, 0, 0, 2, 0, 0},
						{0, 0, 1, 2, 4, 0}};
		System.out.println(hourglassSum(arr));
	}
}
