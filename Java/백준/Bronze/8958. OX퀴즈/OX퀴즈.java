import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        // 배열의 형태로 문자열 입력받기
        String arr[] = new String[sc.nextInt()];      
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.next();
        }

        // O의 개수 세기 
        for (int i = 0; i < arr.length; i++) {

            int count = 0;
            int sum = 0;

            for (int j = 0; j < arr[i].length(); j++) {
                if (arr[i].charAt(j)=='O') {
                    count++;
                    sum += count;
                } else {
                    count = 0;
                }
               
            }  
             System.out.println(sum);
        }
    }
}
