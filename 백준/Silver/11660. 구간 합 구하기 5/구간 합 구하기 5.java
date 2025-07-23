
import java.util.Scanner;
//sout + tap

public class Main {
    public static void main(String[] args)
    {
        // 데이터 입력
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();   // 배열의 차원
        int k = sc.nextInt();   // 질의 개수
        int[][] A = new int[N+1][N+1]; // 행렬

        A[0][0] = 0;
        for(int i =1; i<=N; i++)
        {
            A[0][i]=0;
            A[i][0]=0;
            for(int j =1; j<=N; j++)
            {
                A[i][j] = A[i-1][j] + A[i][j-1] - A[i-1][j-1] + sc.nextInt();
            }
        }
        int x1 = 0; int x2 = 0; int y1 = 0; int y2 = 0;
        for(int i = 0; i<k; i++)
        {
            x1 = sc.nextInt();
            y1 = sc.nextInt();
            x2 = sc.nextInt();
            y2 = sc.nextInt();
            System.out.println(A[x2][y2]-A[x1-1][y2]-A[x2][y1-1]+A[x1-1][y1-1]);
        }


        // 메인 로직

//        // 데이터 출력
//        for (int i = 0; i<N; i++)
//        {
//            System.out.println(A[i]);
//        }

    }
}
