import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int i = 0; i < T; i++) {
			int N = sc.nextInt();
			
			System.out.print("Case #" + (i + 1) + ": ");
			if(N > 4500) {
				System.out.println("Round 1");
			}else if(N > 1000) {
				System.out.println("Round 2");
			}else if(N > 25) {
				System.out.println("Round 3");
			}else {
				System.out.println("World Finals");
			}
		}
		sc.close();
    }
}
