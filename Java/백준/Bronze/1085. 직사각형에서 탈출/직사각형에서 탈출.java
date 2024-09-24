import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();   // 현재의 x좌표
        int y = sc.nextInt();   // 현재의 y좌표
        int w = sc.nextInt();   // 오른쪽 위 꼭짓점의 x좌표
        int h = sc.nextInt();   // 오른쪽 위 꼭짓점의 y 좌표

        sc.close();

        int x_min = Math.min(x, w-x);       // x축 기준의 최소거리
        int y_min = Math.min(y, h-y);       // y축 기준의 최소거리
 
        System.out.println(Math.min(x_min, y_min));

    }
}