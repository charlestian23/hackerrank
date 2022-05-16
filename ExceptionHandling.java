import java.io.*;
import java.util.*;

public class ExceptionHandling
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        try
        {
            int x = input.nextInt();
            int y = input.nextInt();
            try
            {
                System.out.println(x / y);
            }
            catch (ArithmeticException e)
            {
                System.out.println("java.lang.ArithmeticException: / by zero");
            }
        }
        catch (InputMismatchException e)
        {
            System.out.println("java.util.InputMismatchException");
        }
    }
}
