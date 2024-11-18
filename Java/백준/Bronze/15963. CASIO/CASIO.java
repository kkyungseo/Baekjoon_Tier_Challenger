import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();       // N : 필요한 배터리 (최대 10자리 정수까지)
        long M = sc.nextLong();       // M : 가져온 배터리 (최대 10자리 정수까지)
       
        // N, M 이 일치하면 1 출력
        // 그 외에는 0 출력

        int res = 0;

        if ( N == M ) {
            res = 1;
        } else {
            res = 0;
        }

        System.out.println(res);

    }
}
