//Sum of even numbers in an array
package array;
import java.util.*;
public class evenArraySum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr= new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
            if(n%2==0){
                System.out.println("Sum of even numbers is "+arr[i]);
            }
        }
    }
    
}
