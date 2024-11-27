import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 입력조건 
        int N = sc.nextInt();       // N: 후보군 문제의 개수
        
        int excludedCount = 0;      // 제외된 문제 개수를 저장하는 변수

        // 각 문제의 난이도 입력
        for (int i = 0; i < N; i++) {  
            int D = sc.nextInt();   // D: 각 문제의 난이도
            // 난이도가 홀수인지 확인
            if (D % 2 != 0) {       // 홀수라면 제외 대상
                excludedCount++;
            }
        }

        // 출력조건
        // 제외된 문제의 개수
        System.out.println(excludedCount);
        
        sc.close();
    }
}
