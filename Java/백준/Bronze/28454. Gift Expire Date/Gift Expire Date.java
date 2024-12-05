import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");

        // 현재 날짜 입력
        String now = sc.nextLine();
        LocalDate currentDate = LocalDate.parse(now, formatter);        

        // 기프티콘의 개수 입력
        int N = sc.nextInt();
        sc.nextLine();          // 버퍼 비우기

        int validCount = 0;     // validCount : 유효한 기프티콘 개수

        for (int i = 0; i < N; i++) {
            String date = sc.nextLine(); // 기프티콘 유효기간 입력
            try {
                LocalDate gifticonDate = LocalDate.parse(date, formatter); 

                // 유효기간이 현재 날짜와 같거나 이후인 경우 유효한 기프티콘
                if (!gifticonDate.isBefore(currentDate)) {
                    validCount++;
                }
            } catch (DateTimeParseException e) {
                System.out.println("잘못된 날짜 형식");
            }
        }

        // 결과 출력
        System.out.println(validCount);

        sc.close();
    }
}
