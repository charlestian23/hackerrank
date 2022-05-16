import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class BalancedBrackets {

    // Complete the isBalanced function below.
    static String isBalanced(String s) {
        Stack<Character> stack = new Stack<Character>();
        stack.push('x');
        char[] array = s.toCharArray();
        for (int i = 0; i < array.length; i++)
        {
            if ((array[i] == '{' || array[i] == '(' || array[i] == '['))
                stack.push(array[i]);
            else {
                char c = stack.pop();
                if (c == 'x')
                    return "NO";
                else if (c == '{' && array[i] != '}')
                    return "NO";
                else if (c == '(' && array[i] != ')')
                    return "NO";
                else if (c == '[' && array[i] != ']')
                    return "NO";
            }
        }
        if (stack.size() > 1)
            return "NO";
        return "YES";

//        while (array[counter] == '{' || array[counter] == '(' || array[counter] == '[') {
//            stack.push(array[counter]);
//            counter++;
//        }
//        for (int i = counter; i < array.length; i++)
//        {
//
//        }
//        return "YES";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String s = scanner.nextLine();

            String result = isBalanced(s);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
