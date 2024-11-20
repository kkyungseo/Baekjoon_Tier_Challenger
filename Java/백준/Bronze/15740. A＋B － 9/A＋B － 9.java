import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 입력받는 두 정수 A, B
        // -10^10000 ≤ A, B ≤ 10^10000
        int A = sc.nextInt();    
        int B = sc.nextInt();

        System.out.println(A+B);

    }
}