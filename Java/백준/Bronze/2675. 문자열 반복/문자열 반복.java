import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력조건
        int T = sc.nextInt();           // T : 테스트 케이스의 개수 (1 <= T <= 1000)
        
        for (int i = 0; i < T; i++) {
            int R = sc.nextInt();       // R : 문자열 S를 반복하는 횟수 (1 <= R <= 8)
            String S = sc.next();       // S : 입력받는 문자열 (공백으로 구분, 1 <= S <= 20)

            // 출력조건
            // P : 문자열 S의 각 문자를 R번 반복해서 만든 문자열
            StringBuilder P = new StringBuilder();              // 결과 문자열을 저장할 StringBuilder 객체

            for (int j = 0; j < S.length(); j++) {
                char ch = S.charAt(j);                  // 문자열 S의 각 문자에 대해 반복
                for (int k = 0; k < R; k++) {           // 각 문자를 R번 반복
                    P.append(ch);
                }
            }
            
            System.out.println(P);        // 결과 문자열 P 출력
        }
    }
}