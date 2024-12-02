import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        // 입력조건
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] num = new int[N];

        for (int i = 0; i < N; i++) {
            num[i] = Integer.parseInt(br.readLine());
        }

        // 오름차순 정렬
        Arrays.sort(num);

        // 출력조건
        for (int i = 0; i < N; i++) {
            bw.write(num[i] + "\n");
        }
        
        // 출력 버퍼 비우기
        bw.flush();
        bw.close();
        br.close();
    }
}
