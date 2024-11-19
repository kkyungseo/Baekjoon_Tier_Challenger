import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Vigenere cipher
        // 암호화키에 존재하는 알파벳, 평문에 존재하는 알파벳

        // 평문알파벳 - 암호화알파벳의순서 ==> 암호화알파벳의순서의 크기만큼의 앞의 문자
        // 알파벳 리스트가 원형으로 순환
        // 평문의 문자가 공백이면 공백 그대로 출력

        // 첫째 줄, 평문 주어짐 (알파벳 소문자, 공백문자로만 구성/공백포함하여 30000자 이하)
        // 둘째 줄, 암호화키 주어짐 (알파벳 소문자만으로 구성)

        String plaintext = sc.nextLine();       // 평문
        String key = sc.nextLine();             // 암호화 키

        // 암호화된 결과 저장
        StringBuilder result = new StringBuilder(); 

        // 암호화 키의 길이
        int keyLength = key.length(); 

        for (int i = 0, j = 0; i < plaintext.length(); i++) {
            char plainChar = plaintext.charAt(i);

            if (plainChar == ' ') {     // 공백 처리
                result.append(' ');
                j++; // 암호화 키의 인덱스만 증가
            } else {
                char keyChar = key.charAt(j % keyLength);        // 암호화 키의 순환적 적용
                int shift = keyChar - 'a';                       // 암호화 키의 알파벳 순서 계산
                char encryptedChar = (char) ((plainChar - 'a' - shift + 26 - 1) % 26 + 'a'); // 암호화 적용
                result.append(encryptedChar);
                j++; // 암호화 키의 인덱스만 증가
            }
        }

        // 결과 출력
        System.out.println(result.toString());
    }
}
