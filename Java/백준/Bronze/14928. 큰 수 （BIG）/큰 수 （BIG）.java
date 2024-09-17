import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String N = sc.nextLine();

        int div = 20000303;

        int res = calculateRemainder(N,div);
        System.out.println(res);
    }
    private static int  calculateRemainder(String N, int div) {

        int res = 0;

        for (int i = 0; i < N.length(); i++) {
            res = (res * 10 + (N.charAt(i)-'0'))% div;
        }
        return res;
    }

}
