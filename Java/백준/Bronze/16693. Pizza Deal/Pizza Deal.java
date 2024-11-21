import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 받기
        int A1 = sc.nextInt(); // 슬라이스의 면적
        int P1 = sc.nextInt(); // 슬라이스의 가격
        int R1 = sc.nextInt(); // 원형의 반지름
        int P2 = sc.nextInt(); // 원형의 가격

        sc.close();

        // 단위 면적당 가격 계산
        double slicePricePerArea = (double) P1 / A1; // 슬라이스: 가격 / 면적
        double wholePricePerArea = (double) P2 / (Math.PI * R1 * R1); // 원형: 가격 / 면적

        // 결과 비교
        if (slicePricePerArea < wholePricePerArea) {
            System.out.println("Slice of pizza");
        } else if (slicePricePerArea > wholePricePerArea) {
            System.out.println("Whole pizza");
        } else {
            System.out.println(" ");
        }
    }
}
