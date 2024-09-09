import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int[] arr = new int[9];

		for (int i = 0; i < arr.length; i++) {
			arr[i] = scan.nextInt();
		}

		scan.close();
		
		int max = arr[0];
		int maxIndex = 0;
		
		for (int i = 1; i < arr.length; i++) {
			if(arr[i]>max) {
				max = arr[i];
				maxIndex = i;
			}
		}

		System.out.println(max);
		System.out.println(maxIndex+1);

	}
}