import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 조건
        int N = sc.nextInt();       // N : 수의 개수 ( 1 <= N <= 500000 )
        
        // N이 홀수가 아니면, 프로그램 종료
        if (N % 2 == 0) {
            System.out.println("N은 홀수여야 합니다.");
            return;
        }

        int [] arr = new int[N];    // arr : 숫자를 저장하는 배열

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        // 배열 정렬
        Arrays.sort(arr);
        
        // 출력 조건
        // 산술평균 : 소수점 이하 첫째 자리에서 반올림한 값 출력
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];  // 각 요소의 값을 더해야 함
        }
        int avg = (int)Math.round((double)sum / N);    
        
        // 중앙값
        int med = arr[arr.length / 2];    
        
        // 최빈값 : 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값 출력 
        Map<Integer, Integer> freqMap = new HashMap<>();
        int maxFreq = 0;
        for (int num : arr) {
            int freq = freqMap.getOrDefault(num, 0) + 1;
            freqMap.put(num, freq);
            maxFreq = Math.max(maxFreq, freq); 
        }
        List<Integer> modeList = new ArrayList<>();
        for (int key : freqMap.keySet()) {
            if (freqMap.get(key) == maxFreq) modeList.add(key);
        }
        Collections.sort(modeList);  
        // 여러 개일 때 두 번째로 작은 값 선택
        int fre = (modeList.size() > 1) ? modeList.get(1) : modeList.get(0);

        // 범위 : 최댓값 - 최솟값
        int ran = arr[arr.length - 1] - arr[0];   
     
        // 출력
        System.out.println(avg);
        System.out.println(med);
        System.out.println(fre);
        System.out.println(ran);
    }
}
