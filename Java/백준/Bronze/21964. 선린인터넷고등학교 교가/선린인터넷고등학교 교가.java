import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());    // N : 문자열의 길이
        char[] s = br.readLine().toCharArray();     // S : N글자로 이루어진 문자열

        // S의 마지막 5글자를 출력함

        for (int i = n-5; i < n; i++) {
            System.out.print(s[i]);
        }
        System.out.println();
    }
}