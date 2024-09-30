import java.lang.Math;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // A도의 고기를 전자레인지로 B도까지 데우기
        // 데우는 시간은 C초 
        // 고기는 0도를 기준으로 해동여부가 결정됨 (0도이면 해동여부 불명)

        // 고기가 얼어 있고 온도가 0℃ 미만일 때 : 온도가 C초에 1℃씩 오른다.
        // 고기가 얼어 있고 온도가 정확히 0℃일 때 : 얼어 있지 않은 상태로 만드는(해동하는) 데 D초가 걸린다.
        // 고기가 얼어 있지 않을 때 : 온도가 E초에 1℃씩 오른다.

        
        int A = sc.nextInt();       // A : 고기의 온도 (-100 ~ 100)
        int B = sc.nextInt();       // B : 목표온도 (1 ~ 100 / A보다 큰 수)
        int C = sc.nextInt();       // C : 언 고기를 1도 데우는 데 걸리는 시간 (1 ~ 100)
        int D = sc.nextInt();       // D : 얼어 있는 고기를 해동하는 데 걸리는 시간 (1 ~ 100)
        int E = sc.nextInt();       // E : 얼어 있지 않은 고기를 1도 데우는 데 걸리는 시간 (1 ~ 100)
        
        
        // 고기가 B℃까지 데우는 데 걸리는 시간을 초 단위로 출력

        if ( A < 0 ) {
            System.out.println(Math.abs(A)*C + D + B*E);
        } else {
            System.out.println((B-A)*E);
        }
       
    }
}