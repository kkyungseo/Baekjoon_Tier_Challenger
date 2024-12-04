import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 조건
        // 전화번호 끝자리의 네 개의 숫자
        int num1 = sc.nextInt();       
        int num2 = sc.nextInt();       
        int num3 = sc.nextInt();       
        int num4 = sc.nextInt();
        
        if ((num1 == 8 || num1 == 9) && (num4 == 8 || num4 == 9) && (num2 == num3)) {
            System.out.println("ignore");
        } else {
            System.out.println("answer");
        }

        sc.close();

        sc.close();
    }
}