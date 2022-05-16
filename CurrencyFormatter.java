import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class CurrencyFormatter {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        NumberFormat usf = NumberFormat.getCurrencyInstance(Locale.US);
        NumberFormat indiaf = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        NumberFormat chinaf = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat francef = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        
        System.out.println("US: " + usf.format(payment));
        System.out.println("India: " + indiaf.format(payment));
        System.out.println("China: " + chinaf.format(payment));
        System.out.println("France: " + francef.format(payment));
    }
}
