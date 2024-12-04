import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());        // N : N번째 영화
        br.close();

        int num = 666;      // num : 영화의 부제의 숫자
        int cnt = 1;        // cnt : 반복 횟수

        while(N > cnt){
            num++;
            if(String.valueOf(num).contains("666")){ 
                cnt++;
            }
        }

        bw.write(num+"");
        bw.flush();
        bw.close();

    }
}