import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n1 = sc.nextInt();      // n1 : rows of seats in business class
        int k1 = sc.nextInt();      // k1 : seats in business class (each row)

        int n2 = sc.nextInt();      // n2 : rows of seats in economic class
        int k2 = sc.nextInt();      // k2 : seats in economic class (each row)

        sc.close();

        int res = n1 * k1 + n2 * k2;

        System.out.println(res);


    }
}