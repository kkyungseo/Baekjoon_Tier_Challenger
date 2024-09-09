import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] arr = new int[N];
		int count = 0;

		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}

		int find = sc.nextInt();

		for (int i = 0; i < arr.length; i++) {
			if (find == arr[i])
				count += 1;
		}
		System.out.println(count);
	}
}
