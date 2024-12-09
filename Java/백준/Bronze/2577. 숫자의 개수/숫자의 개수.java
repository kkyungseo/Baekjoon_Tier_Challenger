import java.util.Scanner;
 
public class Main {
    
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        // 입력조건
        // 세 개의 자연수 A, B, C ( 100 <= A,B,C <= 1000)
        int value = ( sc.nextInt() * sc.nextInt() * sc.nextInt() );
        String str = Integer.toString(value);
 
        sc.close();
        
        // 출력 조건
        // 0 부터 9 까지의 숫자가 각각 몇 번 쓰였는지 출력

        for (int i = 0; i < 10; i++) {
            int count = 0;
            for (int j = 0; j < str.length(); j++) {
                if ((str.charAt(j)-'0')==i) count++;
            }
            System.out.println(count);
        }

    }
 
}


