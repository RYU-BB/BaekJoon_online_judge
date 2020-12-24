import java.util.Scanner;

public class Main {
	private static int uc(int x, int y) {
		while(y!=0) {
			int remainder = x%y;
			x = y;
			y = remainder;
		}
		return x;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int testT = sc.nextInt();
		long result;
		while(testT-->0) {
			result = 0;
			int inputN = sc.nextInt();
			int numberArr[] = new int[inputN];
			for(int i =0; i<inputN; i++) {
				numberArr[i] = sc.nextInt();
			}
			for(int i=inputN-1; i>=0; i--) {
				for(int j =0; j<i; j++) {
					result+=uc(numberArr[i],numberArr[j]);
					
				}
			}
			System.out.println(result);
		}
	}
}
