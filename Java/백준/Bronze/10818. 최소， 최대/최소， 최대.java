import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int N = scan.nextInt();

		int[] arr = new int[N];

		for (int i = 0; i < arr.length; i++) {
			arr[i] = scan.nextInt();
		}

		scan.close();
		
		int max = arr[0];
		int min = arr[0];	
		
		for (int i = 1; i < arr.length; i++) {
			if(arr[i]>max) {
				max = arr[i];
			}
			if(arr[i]<min) {
				min = arr[i];
			}
		}

		System.out.println(min + " " + max);

	}
}
