import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();                   // N : 전체 사람의 수
        int[][] person = new int[N][2];         // 키와 몸무게를 저장하는 배열
        int[] rank = new int[N];                // 등수를 저장하는 배열
        for (int i = 0; i < N; i++) {
            // 사람의 덩치 : (x,y), (p,q)
            person[i][0] = sc.nextInt();  // x : 몸무게
            person[i][1] = sc.nextInt();  // y : 키
            rank[i] = 1;                  // 초기 등수 설정
        }
        // 덩치 등수 
        // 자신보다 큰 덩치의 사람 k명 ~ 자신의 덩치 등수 : k+1
        // 키, 몸무게가 모두 큰 것이 아니라면 덩치 비교 불가
        // 동점이 있는 경우에는 동일 등수로 책정 (2등이 세 명이면, 다음 등수는 5등)
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i == j) continue;  // 자기 자신과의 비교는 건너뜀
                // 다른 사람과 비교하여 키와 몸무게가 모두 클 경우, 등수 증가
                if (person[i][0] < person[j][0] && person[i][1] < person[j][1]) {
                    rank[i]++;
                }
            }
        }
        // 결과
        for (int i = 0; i < N; i++) {
            System.out.print(rank[i] + " ");
        }
        sc.close();
    }
}
