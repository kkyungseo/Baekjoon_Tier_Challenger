import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 샘플 테스트 개수, 시스템 테스트 개수 입력

        int S1 = sc.nextInt();
        int S2 = sc.nextInt();
        
        boolean wrongAnswer = false;
        boolean whyWrong = false;
        
        // 샘플 테스트 검증
        for (int i = 0; i < S1; i++) {
            int expected = sc.nextInt();  // 예상 출력
            int actual = sc.nextInt();    // 실제 출력
            
            if (expected != actual) {
                wrongAnswer = true;
            }
        }
        
        // 샘플 테스트에서 하나라도 틀리면 
        // "Wrong Answer" 출력 후 종료

        if (wrongAnswer) {
            System.out.println("Wrong Answer");
            return;
        }
        
        // 시스템 테스트 검증
        for (int i = 0; i < S2; i++) {
            int expected = sc.nextInt();   // 예상 출력
            int actual = sc.nextInt();     // 실제 출력
            
            if (expected != actual) {
                whyWrong = true;
            }
        }
        
        // 시스템 테스트에서 하나라도 틀리면 
        // "Why Wrong!!!" 출력
        if (whyWrong) {
            System.out.println("Why Wrong!!!");
        } else {
        // 모든 테스트가 맞으면 "Accepted" 출력
            System.out.println("Accepted");
        }
        
        sc.close();
    }
}
