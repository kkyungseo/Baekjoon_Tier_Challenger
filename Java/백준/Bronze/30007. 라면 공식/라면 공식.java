import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();       // 라면을 끓이는 횟수 : N

        for (int i = 0; i < N; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            int X = sc.nextInt();
            System.out.println(A*(X-1)+B);
        }
        sc.close();
    }

}
