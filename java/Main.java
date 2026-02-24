package java; // 競プロ用コード作成時はpackageを削除する

import java.io.PrintWriter;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

class Main {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        var writer = new PrintWriter(System.out);
        var N = readInt(scanner);

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

    /**
     * 乱数生成器(xoroshiro128++)
     */
    class Xoroshiro128pp {
        private long[] s = {ThreadLocalRandom.current().nextLong(), 0};
        private long rotl(final long x, final int k) {
            return (x << k) | (x >>> (64 - k));
        }
        private long xoroshiro128() {
           var s0 = s[0];
           var s1 = s[1];
           var result = rotl(s0 + s1, 17) + s0;
           s1 ^= s0;
           s[0] = rotl(s0, 49) ^ s1 ^ (s1 << 21);
           s[1] = rotl(s1, 28);
           return result;
        }
        private long nextP2(final long n) {
            var r = n - 1;
            for (var i = 0; i < 6; i++) {
                r |= r >>> (1 << i);
            }
            return r;
        }
        // 指定した値を最大値として乱数を生成します
        public int nextInt(final int mod) {
            var res = 0L;
            var p2mod = nextP2((long) mod);
            do {
                res = xoroshiro128() & p2mod;
            } while (res >= mod);
            return (int) res;
        }
        // int型の範囲で乱数を生成します
        public int nextInt() {
            return nextInt(Integer.MAX_VALUE);
        }
    }
}