import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();

        int res = 0;
        
        for (int i = 0; i < cnt; i++) {
            int num = sc.nextInt();

            if(num == 1) {
                res += 0;
                continue;
            }
            
            int x = 0;
            for (int j = 2; j < num; j++) {
                if( num % j == 0){
                    x++;
                }
            }

            if (x == 0){
                res++;
            }
        }

        System.out.println(res);
    }
}
