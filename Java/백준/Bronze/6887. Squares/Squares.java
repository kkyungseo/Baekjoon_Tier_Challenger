import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();       // N : 가지고 있는 타일의 개수

        // 동일한 크기의 정사각형 타일들을 사용함
        // solid square를 사용하기 위해 테이블에 타이들을 배치하는데,
        // 가장 크게 만들 수 있는 사각형의 변의 길이 구하기 

        int res = 0 ; 

        res = (int)(Math.floor(Math.sqrt(N)));

        System.out.println("The largest square has side length " + res+".");

    }
}
