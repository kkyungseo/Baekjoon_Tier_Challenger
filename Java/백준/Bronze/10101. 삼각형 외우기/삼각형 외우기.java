import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();   // 삼각형의 각 1
        int B = sc.nextInt();   // 삼각형의 각 2
        int C = sc.nextInt();   // 삼각형의 각 3

        sc.close();
        
        String res = null;

        if (A==60 && B==60 && C==60) {
            res = "Equilateral";
        } else if (A+B+C == 180) {
            if (A==B || B==C || C==A) {
                res = "Isosceles";
            } else {
                res = "Scalene";
            }
        } else {
            res = "Error";
        }

        System.out.println(res);




    }
}