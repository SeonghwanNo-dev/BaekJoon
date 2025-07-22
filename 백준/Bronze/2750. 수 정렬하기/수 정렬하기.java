
import java.util.Scanner;
//sout + tap

public class Main {
    public static void main(String[] args)
    {
        // 데이터 입력
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i <N; i++)
        {
            arr[i] = sc.nextInt();
        }

        // 버블 정렬
        int temp = 0;
        for(int i = 0; i<N-1; i++)
        {
            for(int j = 0; j<N-1-i; j++)
            {
                if(arr[j]>arr[j+1])
                {
                    temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }

        // 데이터 출력
        for (int i = 0; i<N; i++)
        {
            System.out.println(arr[i]);
        }

    }
}
