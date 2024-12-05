import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 조건
        int N = sc.nextInt();                   // N: 캐릭터 수 (1 <= N <= 100)
        Integer[] levels = new Integer[N];      // levels : 레벨을 저장할 배열 

        // 캐릭터 레벨 입력
        for (int i = 0; i < N; i++) {
            levels[i] = sc.nextInt();
        }

        // 높은 레벨의 캐릭터부터의 계산을 위한 정렬 
        Arrays.sort(levels, Collections.reverseOrder());

        int levelSum = 0;           // levelSum : 레벨 합계
        int abilityIncrease = 0;    // abilityIncrease : 능력치 상승 합계

        // 상위 42명 or N명의 캐릭터
        for (int i = 0; i < Math.min(N, 42); i++) {  
            int L = levels[i];
            levelSum += L;

            // 능력치 상승 (중첩 조건)
            if (L >= 60) abilityIncrease++;
            if (L >= 100) abilityIncrease++;
            if (L >= 140) abilityIncrease++;
            if (L >= 200) abilityIncrease++;
            if (L >= 250) abilityIncrease++;
        }

        // 출력 조건
        System.out.println(levelSum + " " + abilityIncrease);

        sc.close();
    }
}
