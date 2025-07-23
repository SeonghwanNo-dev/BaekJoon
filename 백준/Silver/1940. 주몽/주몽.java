

import java.util.Scanner;
import java.util.Arrays;
//sout + tap

public class Main {
    public static void main(String[] args)
    {
        // 데이터 입력
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();   // 숫자 개수
        int obj = sc.nextInt();
        int[] A = new int[N];

        for(int i=0; i<N; i++)
        {
            A[i]=sc.nextInt();
        }
        Arrays.sort(A);

        // 투포인터

        int j = N-1;
        int i = 0;
        int count = 0;
        int sum = 0;
        while(j!=i)
        {
            sum = A[i] + A[j];
            if(sum==obj)
            {
                count++;
                j=N-1;
                i++;
            }
            else if(sum>obj) j--;
            else if(sum<obj)
            {
                j = N-1;
                i++;
            };
        }
        System.out.println(count);


        // 메인 로직

//        // 데이터 출력
//        for (int i = 0; i<N; i++)
//        {
//            System.out.println(A[i]);
//        }

    }
}
