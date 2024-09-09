import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int N = scan.nextInt(); 
        String res1 = "long ";
        StringBuilder res2 = new StringBuilder();
        
        for (int i = 0; i < (N/4); i++) {
			res2.append(res1);
		}
        
        System.out.println(res1.repeat(N/4)+"int");
        
    }
}