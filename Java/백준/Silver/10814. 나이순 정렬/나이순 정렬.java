import java.util.Arrays;
import java.util.Scanner;
 
public class Main {
    
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        // 입력조건
        // 회원들이 가입한 순서대로 입력
        int N = sc.nextInt();                       // N : 온라인 저지의 회원의 수 ( 1 <= N <= 100000 )
        String[][] members = new String[N][2];      // members : 회원의 나이, 이름을 저장할 배열

        // 회원 정보 입력
        for (int i = 0; i < N; i++) {
            members[i][0] = sc.next(); // 나이
            members[i][1] = sc.next(); // 이름
        }

        sc.close();

        // 출력 조건 (정렬)
        // 회원 정렬 ~ 회원의 나이가 증가하는 순, 
        //            나이가 같으면 먼저 가입한 사람이 앞에 오는 순서

        Arrays.sort(members, (a, b) -> {
            int ageComparison = Integer.parseInt(a[0]) - Integer.parseInt(b[0]);
            if (ageComparison != 0) {
                return ageComparison; // 나이 기준 정렬
            }
            return 0; // 가입 순서 유지 (기본적으로 배열 순서 보존)
        });

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(members[i][0]).append(" ").append(members[i][1]).append("\n");
        }
        System.out.print(sb);
        
    }
 
}


