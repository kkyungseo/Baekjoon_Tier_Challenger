import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long N = sc.nextLong();          // N : 상금의 금액 (1000의 배수)

        // 규칙 : 상금을 받으면, 전체 금액의 22%는 제세공과금 ~ 나머지 금액 수령
        //         but, 상금의 80%를 필요경비로 인정하게 되면 나머지 20% 중 22%만이 제세공과금이 됨

        // 경우 1 : 전체 상금의 22%를 제세공과금으로 납부하는 경우

        // 경우 2 : 상금의 80%를 필요 경비로 인정받고, 
        //          나머지 금액 중 22%만을 제세공과금으로 납부하는 경우

        long res1 = 0;      // 경우 1
        long res2 = 0;      // 경우 2

        res1 = (long)(N * 0.78);
        res2 = (long)(N * 0.2 * 0.78) + (long)(N * 0.8);

        // 경우1, 2에 대한 값을 공백을 두고 출력
        System.out.println(res1 + " " + res2);

    }
}
