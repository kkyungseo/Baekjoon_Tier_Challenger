import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();       // N : 맵에 존재하는 헬멧의 개수
        int M = sc.nextInt();       // M : 맵에 존재하는 조끼의 개수

        int[] arr1 = new int[N];
        for (int i = 0; i < arr1.length; i++) {
            arr1[i] = sc.nextInt();
        }

        int[] arr2 = new int[M];
        for (int j = 0; j < arr2.length; j++) {
            arr2[j] = sc.nextInt();
        }

        sc.close();

        int max1 = Arrays.stream(arr1).max().orElse(0);
        int max2 = Arrays.stream(arr2).max().orElse(0);

        int res = max1 + max2;

        System.out.println(res);

    }
}