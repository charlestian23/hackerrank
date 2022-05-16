import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class JumpingOnClouds {
	
	 static int jumpingOnClouds(int[] c)
	 {
		 boolean reachedEnd = false;
		 int position = 0;
		 int moves = 0;
		 while (!reachedEnd)
		 {
			 if (c.length - position - 1 <= 0)
			 {
				 reachedEnd = true;
				 moves--;
			 }
			 else if (c.length - position - 2 <= 0)
			 {
				 position++;
				 reachedEnd = true;
			 }
			 else
			 {
				 if (c[position + 2] != 1)
					 position += 2;
				 else
					 position++;
			 }
			 moves++;
		 }
		 return moves;
	 }
	 
	 public static void main(String[] args)
	 {
		 int[] x = {0, 0, 0, 0, 1, 0};
		 System.out.println(jumpingOnClouds(x));
	 }
}
