import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


public class BalancedSystemFilesPartitionSystem {
    public static void main(String[] args)
    {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        System.out.println(map.get(1));
    }

//    public static void main(String[] args) throws IOException {
//        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
//
//        int parentCount = Integer.parseInt(bufferedReader.readLine().trim());
//
//        List<Integer> parent = IntStream.range(0, parentCount).mapToObj(i -> {
//            try {
//                return bufferedReader.readLine().replaceAll("\\s+$", "");
//            } catch (IOException ex) {
//                throw new RuntimeException(ex);
//            }
//        })
//                .map(String::trim)
//                .map(Integer::parseInt)
//                .collect(toList());
//
//        int files_sizeCount = Integer.parseInt(bufferedReader.readLine().trim());
//
//        List<Integer> files_size = IntStream.range(0, files_sizeCount).mapToObj(i -> {
//            try {
//                return bufferedReader.readLine().replaceAll("\\s+$", "");
//            } catch (IOException ex) {
//                throw new RuntimeException(ex);
//            }
//        })
//                .map(String::trim)
//                .map(Integer::parseInt)
//                .collect(toList());
//
//        int result = Result.mostBalancedPartition(parent, files_size);
//
//        bufferedWriter.write(String.valueOf(result));
//        bufferedWriter.newLine();
//
//        bufferedReader.close();
//        bufferedWriter.close();
//    }
}
