
import java.util.Scanner;
//sout + tap

public class Main {
    public static void main(String[] args)
    {
        // 데이터 입력
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int k = sc.nextInt();
        int[] A = new int[N+1];
        int j = 0;
        A[0] = 0;
        for(int i =1; i<=N; i++)
        {
            j = sc.nextInt();
            A[i] = A[i-1] + j;
        }
        int i1 = 0; int i2 = 0;
        for(int i = 0; i<k; i++)
        {
            i1 = sc.nextInt();
            i2 = sc.nextInt();
            System.out.println(A[i2] - A[i1-1]);
        }


        // 메인 로직

//        // 데이터 출력
//        for (int i = 0; i<N; i++)
//        {
//            System.out.println(A[i]);
//        }

    }
}
