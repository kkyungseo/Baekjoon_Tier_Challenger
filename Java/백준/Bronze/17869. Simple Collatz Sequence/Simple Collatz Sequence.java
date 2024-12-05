import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 조건
        long n = sc.nextLong();       // n : 양의 정수 ( 부호 없는 정수 범위 )

        // 문제 규칙
        // SCS 는 양의 정수인 n에서 시작하여 1 까지 도달할 때까지 진행되는 수열
        // 진행되는 현재 수 k 가 짝수라면, 다음 값은 ( k / 2 )
        // 진행되는 현재 수 k 가 홀수라면, 다음 값은 ( k + 1 )
        
        sc.close();

        // 출력 조건
        // 수열이 1에 도달할 때까지 총 단계 수 A(n) 출력 ~ cnt
        
        int cnt = 0;
        
        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;  
            } else {
                n += 1;  
            }
            cnt++;  
        }
        
        System.out.println(cnt);  
    }
}
