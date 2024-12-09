import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
 
public class Main {
    
    public static void main(String args[]) {
        
        List<BigInteger> data = new ArrayList<>();
 
        data.add(BigInteger.ZERO);
        data.add(BigInteger.ONE);

        Scanner sc = new Scanner(System.in);

        // 입력조건
        int N = sc.nextInt();           // N : 입력받는 정수
 
        // 출력 조건
        // 피보나치 수열
        // : 첫째 및 둘째 항이 1이며, 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열
        // : F(0) = 0 , F(1) = 1 일 때, F(N) = F(N-1) + F(N-2)의 계산식이 적용됨
        
        if (0 == N) {
            System.out.println(data.get(0));
            sc.close();
            return;
        }
 
        if (1 == N) {
            System.out.println(data.get(1));
            sc.close();
            return;
        }
 
        for (int i = 2; i <= N; i++) {
            data.add(i, data.get(i - 1).add(data.get(i - 2)));
        }
 
        System.out.println(data.get(N));
        sc.close();
    }
 
}


