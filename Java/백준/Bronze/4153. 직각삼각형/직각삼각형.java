import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);

		while (true) {
			long X = scan.nextInt();
			long Y = scan.nextInt();
			long Z = scan.nextInt();
			
			if (X==0 && Y==0) {
				break;
			}

			if (X * X + Y * Y == Z * Z || Y*Y + Z*Z == X*X || Z*Z + X*X == Y*Y) {
				System.out.println("right");
			} else {
				System.out.println("wrong");
			}
		}
	}
}