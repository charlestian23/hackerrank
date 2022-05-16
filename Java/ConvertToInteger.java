import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ConvertToInteger {

    public static void main(String[] args) {
        String s = "za";
        try
        {
        	System.out.println(Integer.parseInt(s));
        }
        catch (NumberFormatException e)
        {
        	System.out.println("Bad String");
        }
    }
}