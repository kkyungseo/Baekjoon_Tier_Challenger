import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
    
		Scanner in = new Scanner(System.in);
		
		int hour = in.nextInt(); 
		int min = in.nextInt(); 
		
		if(min < 45) {
			hour--;		
			min= 60 - (45 - min); 	
			if(hour < 0) {
				hour = 23;
			}
			System.out.println(hour + " " + min);
		}
		else {
			System.out.println(hour + " " + (min - 45));
		}
	}
}