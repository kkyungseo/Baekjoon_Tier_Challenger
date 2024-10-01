import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); 

        for (int caseNum = 1; caseNum <= t; caseNum++) {
            int[] li = new int[3];

            for (int i = 0; i < 3; i++) {
                li[i] = sc.nextInt();
            }

            Arrays.sort(li);

            System.out.print("Case #" + caseNum + ": ");

            if (li[0] + li[1] <= li[2]) {
                System.out.println("invalid!");
            } else if (li[0] == li[1] && li[1] == li[2]) {
                System.out.println("equilateral");
            } else if (li[0] == li[1] || li[1] == li[2] || li[2] == li[0]) {
                System.out.println("isosceles");
            } else {
                System.out.println("scalene");
            }
        }
        sc.close();
    }
}