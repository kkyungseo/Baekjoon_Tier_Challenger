import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();    
        
        // 조건을 만족하는 수열 : A
        // 수열의 크기 : N

        // 첫째 줄에 N 출력
        // 둘쨰 줄에 A1, A2, ... An 을 공백으로 구분하여 출력
        // 규칙 : A2는 2 가 되어야 함 
        //        ~ A1, A2의 값이 1, 2로 확정
        //        An은 소수가 되어야 함
        
        int[] A = new int[N];
        A[0] = 1;
        A[1] = 2;
        A[N - 1] = 997;       // 1 <= Ai <= 1,000

        for (int i = 1; i < N; i++) {
            if (A[i] == 0) {
                A[i] = A[i - 1] + 1;
            }
        }

        System.out.println(N);
        for (int arr : A) {
            System.out.print(arr + " ");
        }
        sc.close();

    }
}
