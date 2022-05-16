import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class LeftRotation {
	
	static int[] rotLeft(int[] a, int d) 
	{
        int[] x = new int[a.length];
        for (int i = d; i < x.length + d; i++) 
        {
        	int n = i;
        	if (i >= x.length)
        		n = i - x.length;
        	x[i - d] = a[n];
        }
        return x;
    }
	
	public static void main(String[] args)
	{
		int[] x = {1, 2, 3, 4, 5};
		System.out.println(Arrays.toString(rotLeft(x, 4)));
	}
}
