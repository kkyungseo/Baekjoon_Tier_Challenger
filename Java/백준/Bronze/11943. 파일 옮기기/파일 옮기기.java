import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 첫번째 바구니
        int A = sc.nextInt();   // A : 첫번째 바구니 안의 사과
        int B = sc.nextInt();   // B : 첫번째 바구니 안의 오렌지

        // 두번째 바구니
        int C = sc.nextInt();   // C : 두번째 바구니 안의 사과
        int D = sc.nextInt();   // D : 두번째 바구니 안의 오렌지

        sc.close();

        int case1 = A + D;
        int case2 = B + C;

        System.out.println(Math.min(case1, case2));
    }
}