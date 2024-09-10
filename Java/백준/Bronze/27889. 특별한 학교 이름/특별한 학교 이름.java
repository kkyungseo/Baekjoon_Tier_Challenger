import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		
		String abbr = scan.nextLine();
		
		if (abbr.equals("NLCS")) {
			System.out.println("North London Collegiate School");
		} else if (abbr.equals("BHA")) {
			System.out.println("Branksome Hall Asia");
		} else if (abbr.equals("KIS")) {
			System.out.println("Korea International School");
		} else if (abbr.equals("SJA")) {
			System.out.println("St. Johnsbury Academy");
		}
			

	}
}