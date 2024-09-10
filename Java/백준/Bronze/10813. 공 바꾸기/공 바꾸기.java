import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{

        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int arr[] = new int[N];
        int M = scan.nextInt();
        int temp;

        for(int i = 0; i < arr.length; i++) {
            arr[i] = i + 1;                     
        }                                      
        for(int j = 0; j < M; j++) {
            int I = scan.nextInt();
            int J = scan.nextInt();

            temp = arr[I-1];
            arr[I-1] = arr[J-1];
            arr[J-1] = temp;
        }
        for(int k = 0; k <arr.length; k++) {
            System.out.print(arr[k] + " ");
        }
    }
}