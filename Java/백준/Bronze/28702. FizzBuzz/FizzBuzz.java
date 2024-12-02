import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] arr = new String[3];
        int N = 0; // 출력할 숫자

        // 입력 조건
        for (int i = 0; i < 3; i++) {                   // 3개의 문자열 입력받기 ~ arr 에 저장
            arr[i] = sc.nextLine();

            if (arr[i].matches("\\d+")) {              // 숫자 확인 (정규표현식 \\d : 0~9)
                N= Integer.parseInt(arr[i]) + (3 - i);       // 숫자 계산 (문자열을 정수 반환 / 입력 위치에 따른 숫자 보정)
            }
        }

        // 출력 조건
        if (N % 15 == 0) {
            System.out.println("FizzBuzz");
        } else if (N % 3 == 0) {
            System.out.println("Fizz");
        } else if (N % 5 == 0) {
            System.out.println("Buzz");
        } else {
            System.out.println(N);
        }
    }
}
