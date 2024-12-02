import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();       // M : 상근이의 남자친구의 수 ( 1 <= M <= 5 )
        int F = sc.nextInt();       // F : 상근이의 여자친구의 수 ( 1 <= F <= 5 )
        
        while (M != 0 && F != 0) {
            System.out.println(M + F);
            M = sc.nextInt();
            F = sc.nextInt();
        }
        sc.close();
    }
}