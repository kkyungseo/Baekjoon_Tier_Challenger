import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);

        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();
        int num4 = sc.nextInt();
        int num5 = sc.nextInt();

        int ver = ((int)((Math.pow(num1, 2))
                        + (Math.pow(num2, 2))
                        + (Math.pow(num3, 2))
                        + (Math.pow(num4, 2))
                        + (Math.pow(num5, 2))))%10;
        
        System.out.println(ver);

    }
}