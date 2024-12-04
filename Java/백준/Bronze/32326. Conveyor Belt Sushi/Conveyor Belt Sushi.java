import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 조건
        int R = sc.nextInt();       // R : 빨간색 접시의 개수 (각 3달러)
        int G = sc.nextInt();       // G : 초록색 접시의 개수 (각 4달러)
        int B = sc.nextInt();       // B : 파란색 접시의 개수 (각 5달러)
        
        sc.close();

        int C = R * 3 + G * 4 + B * 5;

        System.out.println(C);

    }
}