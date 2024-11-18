import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 지역대회별로 할당된 티켓의 수는 다를 수 있음
        // super region으로 Asia Pacific 과 같은 분류는 site score 파라미터에 의해 산정됨

        // 문제 상황 :
        // 평년과 다르게 Taipie-Hsinchu 지역 대회가 단순화됨

        // UR : 지역 대회에서 최소 한 문제를 푼 대학의 수
        // TR : 지역 대회에서 최소 한 문제를 푼 팀의 수
        // UO : TOPC 에서 최소 한 문제를 푼 대학의 수
        // TO : TOPC 에서 최소 한 문제를 푼 팀의 수

        // site score 파라미터 :
        // = 56UR + 24TR + 14UO + 6TO

        int UR = sc.nextInt();        
        int TR = sc.nextInt();        
        int UO = sc.nextInt();        
        int TO = sc.nextInt();        

        int res = 0;

        res = 56 * UR + 24 * TR + 14 * UO + 6 * TO ;

        System.out.println(res);
        

    }
}
