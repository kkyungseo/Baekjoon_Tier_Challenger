import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        
        if (s.equals("\"") 
            || s.equals("\"\"") 
            || !(s.startsWith("\"") && s.endsWith("\""))) {
            System.out.println("CE");
        } else {
            System.out.println(s.replace("\"", ""));
        }
        
        sc.close();
       
    }
}