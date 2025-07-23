

import java.util.Scanner;
//sout + tap

public class Main {
    public static void main(String[] args)
    {
        // 데이터 입력
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();   // 숫자 개수
        int M = sc.nextInt();   // 나눌 숫자
        int[] S = new int[N+1]; // 합배열

        S[0] = 0;
        for(int i =1; i<=N; i++)
        {
            S[i]=S[i-1]+sc.nextInt();
            S[i]%=M;
        }

        long[] count = new long[M];
        int temp = 0;
        for(int i = 0; i<=N; i++)
        {
            temp = S[i];
            count[temp]++;
        }

        long sum = 0;
        for(int i = 0; i<M; i++)
        {
            if(count[i]>1)
              sum += count[i]*(count[i]-1)/2;
        }
        System.out.println(sum);

        // 메인 로직

//        // 데이터 출력
//        for (int i = 0; i<N; i++)
//        {
//            System.out.println(A[i]);
//        }

    }
}
