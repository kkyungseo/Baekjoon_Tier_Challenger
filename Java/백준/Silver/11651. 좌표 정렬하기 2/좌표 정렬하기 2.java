import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력조건
        int N = sc.nextInt();          
        // N : 점의 개수 ( 1 <= N <= 100000 ) 

        // (xi, yi)를 저장할 배열 생성
        int[][] points = new int[N][2];

        // N개의 줄에는 
        // i번 점의 위치 ( xi, yi ) 의 위치가 주어짐 
        // 좌표는 항상 정수이고, 위치가 같은 두 점은 없음
        // ( -100000 <= xi <= 100000 / -100000 <= yi <= 100000 )
        for (int i = 0; i < N; i++) {
            points[i][0] = sc.nextInt();    // x 좌표 입력
            points[i][1] = sc.nextInt();    // y 좌표 입력
        }

        sc.close(); 

        // 정렬 ( a점과 b 점간의 Comparator )
        Arrays.sort(points, (a, b) -> {

            // y좌표 기준 정렬
            if (a[1] == b[1]) {
                // y좌표가 같은 경우, x좌표 기준 정렬
                return Integer.compare(a[0], b[0]);
            } 
            else {
                // y좌표 기준 정렬
                return Integer.compare(a[1], b[1]);
            }
        });

        // 출력 조건 ( 한 칸 공백으로 x, y 출력 )
        for (int i = 0; i < N; i++) {
            System.out.println(points[i][0] + " " + points[i][1]);
        }
    }
}
