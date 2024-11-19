import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int N = sc.nextInt();       // N : 입력받는 양수 (1 이상 100 이하)
            if (N == 0) break;          // 0이 입력되면 종료

            for (int i = 1; i <= N; i++) {
                for (int j = 0; j < i; j++) {
                    System.out.print("*");     
                }
                // 줄바꿈
                System.out.println();         
            }
        }
        sc.close();
    }
}
