import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class JavaBigInteger {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        BigInteger x = input.nextBigInteger();
        BigInteger y = input.nextBigInteger();
        System.out.println(x.add(y));
        System.out.println(x.multiply(y));
    }
}