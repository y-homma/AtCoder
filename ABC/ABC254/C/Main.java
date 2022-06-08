import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;
import java.util.function.Function;
import java.util.stream.Collectors;

class Main {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var writer = new PrintWriter(System.out);
        var N = readInt(scanner);
        var K = readInt(scanner);
        var A = new int[N];
        var positionMap = new HashMap<Integer, List<Integer>>();
        for (var i = 0; i < N; i++) {
            A[i] = readInt(scanner);
            if (!positionMap.containsKey(A[i])) {
                positionMap.put(A[i], new ArrayList<Integer>());
            } 
            positionMap.get(A[i]).add(i % K);
        }
        Arrays.sort(A);
        var sortedPositionMap = new HashMap<Integer, List<Integer>>();
        for (var i = 0; i < N; i++) {
            if (!sortedPositionMap.containsKey(A[i])) {
                sortedPositionMap.put(A[i], new ArrayList<Integer>());
            } 
            sortedPositionMap.get(A[i]).add(i % K);
        }
        var ans = true;
        for (var entry : sortedPositionMap.entrySet()) {
            var sortedPosition = entry.getValue();
            var beforePosition = positionMap.get(entry.getKey());
            sortedPosition.sort(Comparator.naturalOrder());
            beforePosition.sort(Comparator.naturalOrder());
            if (!sortedPosition.equals(beforePosition)) {
                ans = false;
                break;
            }
        }
        writer.println(ans ? "Yes" : "No");
        
        scanner.close();
        writer.flush();
    }

    /**
     * 入力をInt型で受け取ります
     * @param scanner Scanner
     * @return 入力値(int)
     */
    static Integer readInt(final Scanner scanner) {
        return Integer.parseInt(scanner.next());
    }
}
