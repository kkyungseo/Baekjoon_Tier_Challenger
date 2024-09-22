import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
        int n = sc.nextInt();             


        for (int i = 0; i < n; i++) {
            String name = sc.next(); 
            System.out.print(name.charAt(0));
            System.out.println(name.charAt(name.length()-1));
        }
        sc.close();
        
	}
}