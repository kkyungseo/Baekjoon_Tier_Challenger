import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();       // 별의 개수 : N
        sc.close();

        for (int i = 0; i < N; i++) {
            for (int k = N-i; k < N; k++) {
                System.out.print(" "); 
            }             
            for (int j = i; j < N ; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
	}
}