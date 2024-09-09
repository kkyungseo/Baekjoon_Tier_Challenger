import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt(); 
        int sum = 0;
        
        for (int i = 1; i <= num; i++) {
			sum += i;
		}
        System.out.println(sum);
            
    }
}
