import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int X = scan.nextInt(); 
        int N = scan.nextInt(); 
        int total = 0;

        for(int i = 0; i < N; i++){
            int a = scan.nextInt(); 
            int b = scan.nextInt(); 
            total += a * b;
        }
        if(total == X){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}