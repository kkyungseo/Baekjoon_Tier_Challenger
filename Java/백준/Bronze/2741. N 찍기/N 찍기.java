import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력조건
        int N = sc.nextInt();       // N : 자연수 ( 1 <= N <= 100000 )

        sc.close();

        // 출력조건
        // 첫째 줄부터 N번째 줄까지 차례대로 출력

        int i = 1;
        
		while(i<= N) {
			System.out.println(i);
			i++;
		}

    }
}
