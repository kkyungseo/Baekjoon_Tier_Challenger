import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt();               // R : 반지름 (10000보다 작거나 같은 자연수)         
        sc.close();

        double res1 = Math.PI * R * R;
        double res2 = 2 * R * R;

        // 출력
        // : 첫째줄에는 '유클리드 기하학'에서의 반지름 R인 원의 넓이
        System.out.println(res1);
        // : 둘째줄에는 '택시 기하학'에서 반지름 R인 원의 넓이 
        System.out.println(res2);
      
    }
}
