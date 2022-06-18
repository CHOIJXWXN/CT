import java.io.*;
import java.util.*;

public class test {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      
      int D = Integer.parseInt(st.nextToken());
      int M = 3;
      int F = Integer.parseInt(st.nextToken());
      
      int[] friend = new int[F];
      
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < F; i++) {
         friend[i] = Integer.parseInt(st.nextToken())-1;
      }
      
      int[][] dp = new int[M][5]; //(날짜정보, 외출여부, No외출, 하루외출, 연속 외출)
      // 외출여부: 2면 무조건 나감, 1이면 자율, 0이면 안나감
      dp[0][0]=1;
      dp[0][1]=1;
      dp[1][1]=1;
      dp[1][0]=1;
      int dpIdx=2;
      
      day:for (int i = 0; i < D; i++) {
         dp[dpIdx][0] = Integer.parseInt(br.readLine());
         
         for (int j = 0; j < F; j++) {
            // 친구와의 약속날짜면 무조건 나감
            if (friend[j]==i) {
               dp[dpIdx][1] =2; 
               // XO
               dp[dpIdx][3] =  dp[(dpIdx+2)%M][1]!=2?dp[(dpIdx+2)%M][2]+1:0;
               // XOO
               dp[dpIdx][4] = dp[(dpIdx+2)%M][1]!=0?dp[(dpIdx+2)%M][3]+1:0;
               dpIdx=(dpIdx+1)%M;
               continue day;
            }
         }
         
         // 날씨 외출 안됨
         if ((dp[dpIdx][0]==0)  ||  (dp[(dpIdx+2)%M][0]==0&&dp[(dpIdx+1)%M][0]==0)) {
            dp[dpIdx][1] =0; 
            // 안나감
            dp[dpIdx][2] = Math.max(Math.max(dp[(dpIdx+2)%M][2], dp[(dpIdx+2)%M][3]), dp[(dpIdx+2)%M][4]);
         } else {
            dp[dpIdx][1] =1; 
            // XO
            dp[dpIdx][3] = dp[(dpIdx+2)%M][1]!=2?dp[(dpIdx+2)%M][2]+1:0;
            // XOO
            dp[dpIdx][4] = dp[(dpIdx+2)%M][1]!=0?dp[(dpIdx+2)%M][3]+1:0;
            
            dp[dpIdx][2] = Math.max(Math.max(dp[(dpIdx+2)%M][2], dp[(dpIdx+2)%M][3]), dp[(dpIdx+2)%M][4]);
         }
         dpIdx=(dpIdx+1)%M;

      }
      System.out.println(Math.max(Math.max(dp[(dpIdx+2)%M][2], dp[(dpIdx+2)%M][3]), dp[(dpIdx+2)%M][4]));
      
      
      
   }
   
//   static boolean check(int[][] dp, int dpIdx) {
//      int M=3;
//      if ((dp[dpIdx][0]==0)  ||  (dp[(dpIdx-1)%(M+1)][0]==0&&dp[(dpIdx-1)%(M+1)][0]==0)) {
//         return false;
//      } else return true;
//   }
}