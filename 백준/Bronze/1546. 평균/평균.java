import java.util.Scanner;

public class Main {
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int sum = 0;
		int m = 0;
		int i = 0;

		for (int j =0; j<N; j++)
		{
		    i = sc.nextInt();
		    if (m<i) m=i;
		    sum+=i;
		}
		double avg = ((double)sum/m*100)/N;
		System.out.println(avg);
	}
}
