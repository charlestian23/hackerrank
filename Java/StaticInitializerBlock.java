import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StaticInitializerBlock {

static boolean flag = true;
static int B;
static int H;

static {
    Scanner scanner = new Scanner(System.in);
    B = scanner.nextInt();
    H = scanner.nextInt();
    if (B < 0 || H < 0)
		try {
			throw new Exception("Breadth and height must be positive");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			flag = false;
		}
}

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class

