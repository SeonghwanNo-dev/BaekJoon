
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();

		int[][] D = new int[n+1][n+1];
		
		
		
		// 합배열 만들기
		for(int i1 =0; i1<n; i1++)
		{
			for(int i2=0;i2<n;i2++) {
				// 패딩 만들기
				D[0][i2]=0;
				D[i2][0]=0;	
				D[i1+1][i2+1] = D[i1][i2+1] + D[i1+1][i2] - D[i1][i2] + sc.nextInt();
			}
		}
		
		int x1 = 0;
		int x2 = 0;
		int y1 = 0;
		int y2 = 0;
		int PrefixSum = 0;
		// 구간 합 구하기
		for (int i1 = 0; i1<m; i1++)
		{
			x1 = sc.nextInt();
			y1 = sc.nextInt();
			x2 = sc.nextInt();
			y2 = sc.nextInt();
			
			PrefixSum = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1];
			System.out.println(PrefixSum);
		}

		
	}

}
