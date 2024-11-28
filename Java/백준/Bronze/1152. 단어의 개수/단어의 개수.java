import java.util.Scanner;
import java.util.StringTokenizer;
 
public class Main {
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
 
        // 입력조건
        // 문장 입력받기 ( 공백포함 가능성 O )
		String str = sc.nextLine();
		sc.close();

        // 공백기준으로 str 나누기
		StringTokenizer st = new StringTokenizer(str," ");
		
        // 나눠진 str을 토큰으로 개수 세기
		System.out.println(st.countTokens());	
		
	}
 
}