import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();       // N : 시험을 본 과목의 개수
        int[] scr = new int[N];     // 성적을 저장할 배열

        int maxScore = 0;           // 가장 큰 성적

        // 성적 입력 받기
        for (int i = 0; i < N; i++) {
            scr[i] = sc.nextInt();
            if (scr[i] > maxScore) {
                maxScore = scr[i];  // 최대 점수 갱신
            }
        }

        // 성적을 가장 큰 성적으로 나눈 후 100을 곱하고 평균 구하기
        double sum = 0;
        for (int i = 0; i < N; i++) {
            sum += (double) scr[i] / maxScore * 100;
        }

        System.out.println(sum/N);

        sc.close();
    }
}
