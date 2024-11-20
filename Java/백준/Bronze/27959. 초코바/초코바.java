import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();       // N : 100원 동전의 개수 ( 1 <= N <= 100 )
        int M = sc.nextInt();        // M : 초코바의 가격 ( 1 <= M <= 10000 )

        if (N*100 >= M) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        sc.close();

    }
}

