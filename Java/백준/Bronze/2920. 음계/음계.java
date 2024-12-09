import java.util.Scanner;
 
public class Main {
    
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        // 입력조건
        // 입력받은 음계 배열
        int[] arr = new int[8];
        for (int i = 0; i < 8; i++) {
            arr[i] = sc.nextInt();
        }
 
        // 출력 조건
        // ascending : 1부터 8까지 차례대로 연주
        // descending : 8부터 1까지 차례대로 연주
        // mixed : 위의 두 경우가 아닌 경우

        // 초기 상태를 판단하기 위한 변수
        boolean ascending = true;
        boolean descending = true;

        // 배열 순회하면서 비교
        for (int i = 1; i < 8; i++) {
            if (arr[i] > arr[i - 1]) {
                descending = false;         // 증가하면 내림차순이 아님
            } else if (arr[i] < arr[i - 1]) {
                ascending = false;          // 감소하면 오름차순이 아님
            }
        }

        // 결과 출력
        if (ascending) {
            System.out.println("ascending");
        } else if (descending) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }

        sc.close();
    }
 
}


