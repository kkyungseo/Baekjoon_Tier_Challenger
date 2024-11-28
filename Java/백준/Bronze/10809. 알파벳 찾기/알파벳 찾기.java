import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
 
        // 입력조건
        // 알파벳 소문자로만 이루어진 단어 S ( 길이는 100이 넘지 않음 )
		String S = sc.nextLine();  
        int[] position = new int[26]; 
        // 알파벳 a-z에 대한 위치 저장 배열 ( 알파벳의 개수가 26개 )
        
        // 출력조건
        // 단어 S가 주어졌을 때,
        // 각 알파벳 소문자 a-z가 단어에 처음 등장하는 위치를 출력함
        // ( 특정 알파벳이 단어에 없다면 -1을 출력 )
        // 알파벳 순서대로 공백으로 구분하여 나열

        // 배열 초기화: -1로 설정
        for (int i = 0; i < 26; i++) {
            position[i] = -1;
        }
        
        // 문자열 순회: 각 문자의 첫 등장 위치 기록
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i); // 현재 문자
            int index = c - 'a';  // 'a'를 기준으로 한 알파벳 인덱스 계산
            
            // 해당 문자가 아직 기록되지 않았다면 현재 인덱스 기록
            if (position[index] == -1) {
                position[index] = i;
            }
        }
        
        // 결과 출력
        for (int i = 0; i < 26; i++) {
            System.out.print(position[i] + " ");
        }
        
		sc.close();
		
	}
    
}