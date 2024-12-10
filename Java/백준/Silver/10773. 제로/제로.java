import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        // 입력 조건
        int K = sc.nextInt();                   // K : 정수, 줄의 개수 (1 ≤ K ≤ 100,000)
        Stack<Integer> stack = new Stack<>();   // num : 입력받는 K개의 정수를 저장하는 스택

        for (int i = 0; i < K; i++) {
            int N = sc.nextInt();
            if (N == 0) {
                stack.pop();            // 0이면, 가장 최근 숫자를 지움
            } else {
                stack.push(N);          // 0이 아니면, 숫자를 추가
            }
        }
        sc.close();

        // 출력 조건
        int sum = 0;
        for (int num : stack) {
            sum += num;
        }
        System.out.println(sum);        // sum : 최종적으로 적어 낸 수의 합
    }
}
