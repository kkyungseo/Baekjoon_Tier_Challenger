import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // two space-separated integers M and K
        // M : number of medals
        // K : number of kids

        int M = sc.nextInt();
        int K = sc.nextInt();

        if (M%K==0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
    }
}