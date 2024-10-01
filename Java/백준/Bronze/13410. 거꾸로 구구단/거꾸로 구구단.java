import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int K = sc.nextInt();
        
        int max = 0;
        
        for (int i = 1; i <= K; i++) {
            
            int product = N * i;

            // 숫자를 문자열로 변환 후 뒤집기
            String reversedStr = new StringBuilder(String.valueOf(product)).reverse().toString();
            int reversedNum = Integer.parseInt(reversedStr);
            
            // 최댓값 계산
            if (reversedNum > max) {
                max = reversedNum;
            }
        }
        
        // 최댓값 출력
        System.out.println(max);
        
        sc.close();
    }
}
