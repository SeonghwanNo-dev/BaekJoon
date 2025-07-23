
import java.util.Scanner;
//sout + tap

public class Main {
    public static void main(String[] args)
    {
        // 데이터 입력
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();
        int sum = 0;
        char[] s = S.toCharArray();
        for(int i = 0; i <N; i++)
        {
            sum+=s[i]-'0';
        }
        System.out.println(sum);

//        int[] A = new int[N+1];
//        int sum = 0;
//        for(int i = 0; i <N; i++)
//        {
//            A[i] = sc.nextInt();
//            sum+=A[i];
//        }
//        System.out.println(sum);


        // 메인 로직

//        // 데이터 출력
//        for (int i = 0; i<N; i++)
//        {
//            System.out.println(A[i]);
//        }

    }
}
