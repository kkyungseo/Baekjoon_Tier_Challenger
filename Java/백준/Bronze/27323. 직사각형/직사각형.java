import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();   // 직사각형의 세로
        int B = sc.nextInt();   // 직사각형의 가로

        sc.close();

        System.out.println(A*B);


    }
}