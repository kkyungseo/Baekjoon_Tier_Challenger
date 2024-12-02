import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        sc.close();

        System.out.println(A + B - C);
        System.out.println(Integer.parseInt(String.valueOf(A) + String.valueOf(B)) - C);
    }
}
