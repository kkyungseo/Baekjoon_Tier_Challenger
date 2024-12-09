import java.util.HashSet;
import java.util.Scanner;
 
public class Main {
    
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        HashSet<Integer> h = new HashSet<Integer>();

        // 입력조건
        // 10개의 숫자를 입력받고, 42로 나눈 나머지를 구함
        for (int i = 0; i < 10; i++) {
            h.add(sc.nextInt() % 42);
        }
 
        sc.close();

        // 출력 조건
        // 42로 나눈 나머지를 구해서 서로 다른 값이 몇 개 있는지 출력

        System.out.println(h.size());
        
    }
 
}


