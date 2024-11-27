import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 입력조건
        // 첫 번째 줄 : int R (레귤러 박스 개수)
        // 두 번째 줄 : int S (스몰 박스 개수)

        int R = sc.nextInt();       
        int S = sc.nextInt();       

        // 컵케이크 박스의 크기 : 레귤러 = 8개 / 스몰 = 3개

        // 문제상황
        // 28명의 학생이 있다면 최소 28개의 컵케이크가 필요한 것

        // 출력조건
        // 학생 1명이 컵케이크 1개를 받을 때 컵케이크가 얼마가 남을지 구하기

        System.out.println(( R * 8 + S * 3 ) - 28 );
       
        sc.close();
    }
}
