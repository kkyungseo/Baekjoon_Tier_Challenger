import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {

            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            if (a == b && b == c) {
                if (a == 0)
                    break;
                System.out.println("Equilateral");
            } else if (a + b <= c || b + c <= a || c + a <= b) {
                System.out.println("Invalid");
            } else if (a != b && b != c && c != a) {
                System.out.println("Scalene");
            } else {
                System.out.println("Isosceles");
            }
        }
        sc.close();

    }
}