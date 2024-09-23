import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();       // 숫자의 자릿수 입력
        String numbers = sc.next(); // 숫자 문자열 입력

        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += numbers.charAt(i) - '0'; 
        }

        System.out.println(sum); 
        sc.close();

    }
}