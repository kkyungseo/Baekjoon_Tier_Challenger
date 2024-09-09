import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int N = scan.nextInt();
		int X = scan.nextInt();

		int[] arr = new int[N];

		for (int i = 0; i < arr.length; i++) {
			arr[i] = scan.nextInt();
		}

		scan.close();

		for (int i = 0; i < arr.length; i++) {
			if (arr[i] < X) {
				System.out.println(arr[i]);
			}
		}

	}
}