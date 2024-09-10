import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int N = scan.nextInt();
		
		int[] List = new int[6];
		
		for (int i = 0; i < 6; i++) {
			List[i] = scan.nextInt();
		}
		
		int T = scan.nextInt();
		int P = scan.nextInt();
		int res = 0;
		for (int i = 0; i < 6; i++) {
			res += List[i] / T;
			if (List[i] % T != 0) {
				res++;
			}
		}
		System.out.println(res);
		System.out.println(N / P + " " + N % P);
	}
}