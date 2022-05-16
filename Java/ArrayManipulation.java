import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class ArrayManipulation {
    static long arrayManipulation(int n, int[][] queries) {
        long[] array = new long[n];

        System.out.println(queries.length);

        for (int i = 0; i < queries.length; i++) {
            System.out.println(queries[0][1] + " " + i);
            int lower = queries[i][0];
//            System.out.println(lower);
            int upper = queries[i][1];
//            System.out.println(upper);
            long sum = queries[i][2];
//            System.out.println(sum);
            array[lower - 1] += sum;
            if (upper < n)
                array[upper] -= sum;
        }

        long max = 0;
        long temp = 0;

        for (int i = 0; i < n; i++) {
            temp += array[i];
            if (temp > max)
                max = temp;
        }

        return max;
    }

//		ArrayList<Long> array = new ArrayList<Long>();
//		for (int i = 0; i < n; i++)
//			array.add(0L);
//
//		for (int[] a : queries)
//			for (int i = a[0] - 1; i < a[1]; i++)
//				array.set(i, array.get(i) + (long) a[2]);
//
//		return Collections.max(array);

//		long[] array = new long[n];
//	    long max = 0L;
//        for (int[] a : queries)
//        {
//            for (int i = a[0] - 1; i < a[1]; i++)
//            {
//                array[i] += (long) a[2];
//                if (array[i] > max)
//                	max = array[i];
//            }
//        }
//        return max;

//        long max = array[0];
//        for (long i : array)
//            if (i > max)
//                max = i;
//        return max;

//		long max = array[0];
//		for (long i : array)
//			if (i > max)
//				max = i;
//		return max;

    public static void main(String[] args) {
//		10 3
//		1 5 3
//		4 8 7
//		6 9 1
        int[][] x = {{10, 3},
                {1, 5, 3},
                {4, 8, 7},
                {6, 9, 1}};
        System.out.println(arrayManipulation(10, x));
    }
}
