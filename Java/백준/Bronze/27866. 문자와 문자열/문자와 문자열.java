import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String st = sc.nextLine();
        int n = sc.nextInt()-1;  
        
        System.out.println(st.charAt(n));
    
        sc.close(); 
    }
}
