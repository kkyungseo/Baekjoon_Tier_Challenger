import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N : 데이터셋 라인의 개수 (초기입력)
        int N = sc.nextInt();

        // 각각의 데이터 셋은 X Y 를 포함한 라인을 가짐
        for (int i = 0; i < N; i++) {
            // X : 좀비가 먹는 뇌의 개수
            // Y : 좀비가 생존을 위해 필요로 하는 뇌의 개수
            int X = sc.nextInt();
            int Y = sc.nextInt();

            // X >= Y : "MMM BRAINS" 출력
            // X < Y : "NO BRAINS" 출력
            if (X >= Y) {
                System.out.println("MMM BRAINS");
            } else {
                System.out.println("NO BRAINS");
            }
        }
    }
}
