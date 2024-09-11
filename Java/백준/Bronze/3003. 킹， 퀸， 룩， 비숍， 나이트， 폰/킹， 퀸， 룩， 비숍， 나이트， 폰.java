import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int pieceK = scan.nextInt();	
		int pieceQ = scan.nextInt();	
		int pieceL = scan.nextInt();	
		int pieceB = scan.nextInt();	
		int pieceN = scan.nextInt();	
		int pieceP = scan.nextInt();	
		
		System.out.print((1-pieceK)+" ");
		System.out.print((1-pieceQ)+" ");
		System.out.print((2-pieceL)+" ");
		System.out.print((2-pieceB)+" ");
		System.out.print((2-pieceN)+" ");
		System.out.print((8-pieceP));
		
	}
}