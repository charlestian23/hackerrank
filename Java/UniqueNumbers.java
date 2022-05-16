import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;

public class UniqueNumbers 
{
	public static void main(String[] args)
	{
		HashSet<Integer> h = new HashSet<Integer>();
		int size = (int) Math.round(Math.random() * (1000 - 2) + 2);
		System.out.println(size);
		while (h.size() < size)
		{
			int n = (int) (Math.random() * 100000);
//			System.out.println(n);
			if (!h.contains(n))
				h.add(n);
//			System.out.println(h.size());
		}
//		System.out.println(h.toString());
		Integer[] array = h.toArray(new Integer[h.size() + 1]);
		System.out.println(Arrays.toString(array));
//		int counter = 0;
//		for (int i : temporary)
//		{
//			array[counter] = i;
//			counter++;
//		}
		Collections.min(h);
	}
}
