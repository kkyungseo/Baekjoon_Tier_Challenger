import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // 스시의 종류 : 26가지 (A~Z에 대응) ~ 손님이 먹고 싶어하는 스시는 문자열로 주어짐
        // 초밥집의 의자 : ( N + 1 ) 개
        // 초밥집의 접시 : ( N + 1 ) 개
        // 운영진 : N 명 ~ 자신의 순서에 맞는 스시만 먹거나 접시에 손대지 않음

        // 규칙
        // S0에는 셰프가 위치
        // 셰프는 자신의 앞에 있는 접시가 비어 있으면 스시 1개 제작
        // 모든 손님이 유한한 시간안에 식사를 마칠 수 있으밍 보장되면, 스시 제작 중지

        // 출력
        // 모든 손님들이 유한한 시간 안에 식사를 마치기 위해 셰프가 만들어야 하는 스시의 최소 개수

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        int cnt = 0;

        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            cnt += s.length();
        }

        System.out.println(cnt);

        sc.close();

    }
}
