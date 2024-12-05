import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 조건
        int N = sc.nextInt();       // N : 빵묶음의 개수 ( 1 <= N <= 50 )
        int K = sc.nextInt();       // K : 빵묶음 하나에 들어있는 빵의 개수 ( 1 <= K <= 50 )
        int P = sc.nextInt();       // P : K개의 빵 중 크림이 없는 빵의 개수 ( 1 <= P <= K ) ~ P개 미만

        // 문제 조건
        // 크림이 없는 빵이 한 묶음에 P개 이상 있다면, 그 묶음은 팔 수 없음

        // 빵에 대한 배열 생성
        int[] bread = new int[N*K];
        
        // 빵에 대한 정보 입력
        for (int i = 0; i < N*K; i++) {
            int input;
            do {
                input = sc.nextInt();
                // 0과 1만 입력받도록 제한
                if (input != 0 && input != 1) {
                    System.out.println("0 또는 1만 입력 가능합니다. 다시 입력해주세요.");
                }
            } while (input != 0 && input != 1); 
                // 입력이 0이나 1일 때까지 반복
            bread[i] = input;
        }

        // 빵묶음 검사

        int S = 0;      // S : 팔 수 있는 빵묶음 

        for (int i = 0; i < N; i++) {
            int C = 0;        // C : 각 묶음에서 크림없는 빵의 개수

            // K개의 빵을 하나의 묶음으로 검사
            for (int j = 0; j < K; j++) {
                if (bread[i * K + j] == 0) {  // 크림이 없는 빵
                    C++;
                }
            }

            // 크림 없는 빵의 개수가 P 미만이면 팔 수 있음
            if (C< P) {
                S++;
            }
        }

        System.out.println(S);

        sc.close();

    }
}
