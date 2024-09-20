import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 숫자와 콤마로만 이루어진 문자열 S
        String S = sc.nextLine();
        // S의 문자열을 ,를 기준으로 split
        String[] arr = S.split(",");
        
        // 숫자의 합을 더할 sum
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            int num = Integer.parseInt(arr[i]);
            sum += num;
        }

        System.out.println(sum);
        
    }
}