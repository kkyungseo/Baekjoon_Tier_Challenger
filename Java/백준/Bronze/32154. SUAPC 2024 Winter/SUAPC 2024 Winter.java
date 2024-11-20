import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // N : 등수 ( 1 <= N <= 10 )
        sc.close();

        // 패널티 데이터
        String[][] res = {
                { "11", "A B C D E F G H J L M" }, 
                { "9", "A C E F G H I L M" }, 
                { "9", "A C E F G H I L M" },
                { "9", "A B C E F G H L M" },
                { "8", "A C E F G H L M" },
                { "8", "A C E F G H L M" },
                { "8", "A C E F G H L M" },
                { "8", "A C E F G H L M" },
                { "8", "A C E F G H L M" },
                { "8", "A B C F G H L M" }
        };

        // 등수는 1부터 시작하지만 배열 인덱스는 0부터 시작하므로 -1 필요
        if (N >= 1 && N <= 10) {
            // res 배열에서 N-1 번째 데이터를 출력
            System.out.println(res[N - 1][0]);
            System.out.println(res[N - 1][1]);
        } else {
            System.out.println(" ");
        }
    }
}
