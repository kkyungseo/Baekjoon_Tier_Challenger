import java.math.BigInteger;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		BigInteger n = scan.nextBigInteger();		// 최백준 조교가 가진 돈 : n
		BigInteger m = scan.nextBigInteger();		// 돈을 받으러 온 생명체의 수 :m
		
		System.out.println(n.divide(m));
		System.out.println(n.remainder(m));
		
		scan.close();
	}
}