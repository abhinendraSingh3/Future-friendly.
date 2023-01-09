import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

  public void check(int a){
      if (a%2!=0){
          System.out.println("Weird");
      }
      else if(a%2==0 && a>=2 && a<=5){
          System.out.println("Not Weird"); 
      }
      else if(a%2==0 && a>=6 && a<=20){
          System.out.println("Weird"); 
      }
       else if(a%2==0 && a>20){
          System.out.println("Not Weird"); 
      }
  }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();
        Solution l=new Solution();
        l.check(N);
    }
}
