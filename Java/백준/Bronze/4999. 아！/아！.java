import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		String patient = scan.nextLine();		
		String doctor = scan.nextLine();	
		
		scan.close();
		
		if (patient.length() >= doctor.length()) {
			System.out.println("go");
		} else {
			System.out.println("no");
		}
		
	}
}