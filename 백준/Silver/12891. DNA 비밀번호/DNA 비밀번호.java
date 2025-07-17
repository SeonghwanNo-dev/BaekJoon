
import java.util.Scanner;
import java.util.Arrays; 

public class Main {
	public static void main(String[] args) {
		
		// userInput layer
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();	// 문자 배열 사이즈
		int m = sc.nextInt();	// 윈도우 사이즈
		char[] s = new char[n];
		String s_0 = sc.next();
		s =s_0.toCharArray();
		
		int[] num_1 = new int[4];
		int[] num_2 = new int[4];
		
		for (int i=0; i<4; i++)
		{
			num_2[i] = sc.nextInt();
		}
		
		
		// 윈도우 만들기
		int i=0;
		int j=0;
		int count = 0;
		for(int k=0; k<m; k++)
		{
			if(s[k]=='A') num_1[0]++;
			else if(s[k]=='C') num_1[1]++;
			else if(s[k]=='G') num_1[2]++;
			else if(s[k]=='T') num_1[3]++;
		}
		if (num_1[0]>=num_2[0] && num_1[1]>=num_2[1] && num_1[2]>=num_2[2] && num_1[3]>=num_2[3])
			count++;
		j=m;
		
		
		// 윈도우 슬라이딩 -> 맨 앞 삭제, 맨 뒤 추가
		while(j<n) {
			// 맨 앞 삭제
			if(s[i]=='A') num_1[0]--;
			else if(s[i]=='C') num_1[1]--;
			else if(s[i]=='G') num_1[2]--;
			else if(s[i]=='T') num_1[3]--;
			i++;
			// 맨 뒤 추가
			if(s[j]=='A') num_1[0]++;
			else if(s[j]=='C') num_1[1]++;
			else if(s[j]=='G') num_1[2]++;
			else if(s[j]=='T') num_1[3]++;
			j++;
			
			// 윈도우 내부 검사
			if (num_1[0]>=num_2[0] && num_1[1]>=num_2[1] && num_1[2]>=num_2[2] && num_1[3]>=num_2[3])
				count++;
		}
		
		
		System.out.println(count);
	}

}