import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class IPRegex
{

    public static void main(String[] args){
            String IP = "000.12.12.034";
            System.out.println(IP.matches("\\d{1,2,3}" + "\\." + "\\d{1,2,3}" + "\\." + "\\d{1,2,3}" + "\\." + "\\d{1,2,3}"));

    }
}

//class myRegex
//{
//	String pattern()
//	{
//		return 
//	}
//}