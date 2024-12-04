import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 조건
        // 현재 시간
        int A = sc.nextInt();       // A : 현재 시 (0 <= A <= 23)
        int B = sc.nextInt();       // B : 현재 분 (0 <= B <= 59)
        int C = sc.nextInt();       // C : 현재 초 (0 <= C <= 59)
        // 조리 시간
        int D = sc.nextInt();       // D : 요리에 필요한 시간 (초단위 / 0 <= D <= 500000)

        sc.close();

        int time = A * 3600 + B * 60 + C + D;

        int h = (time / 3600) % 24;   
        int m = (time % 3600) / 60;   
        int s = time % 60;            

        System.out.println(h + " " + m + " " + s);
    }
}
