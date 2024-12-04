import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();       // T : 테스트 데이터의 개수 

        // 입력조건 ( H x W 형태 호텔 )
        for (int i = 0; i < T; i++) {
            int H = sc.nextInt();       // H : 층의 수 
            int W = sc.nextInt();       // W : 방의 개수 
            int N = sc.nextInt();       // N : N번째 손님
            // ( 방의 번호 )
            // YXT 혹은 YYXX 의 형태 
            // Y, YY : 층수
            // X, XX : 엘리베이터부터 세었을 때의 개수
            int X = (N - 1) / H + 1;    // X: 호수 (0부터 시작하는 인덱스 보정)
            int Y = (N - 1) % H + 1;    // Y: 층수 (1부터 시작)
            // 출력조건
            // N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램
            System.out.println( Y * 100 + X );
        }
        sc.close();
    }
}
