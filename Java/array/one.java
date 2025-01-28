
//printing even numbers and then odd numbers
package array;
import java.util.*;
public class one {
    public static void main(String[] args) {
        //Scanner sc = new Scanner(System.in);
        //int[] arr = new int[10];
        int[]arr = {1,2,3,4,5,6,7,8};
        System.out.println("Even numbers are: ");
        for(int i =0;i<arr.length;i++){
            //arr[i] = sc.nextInt();
            if(arr[i]%2==0){
                System.out.println(arr[i]);
            }
        }
        System.out.println("Odd numbers are: ");
        for(int i =0;i<arr.length;i++){
            if(arr[i]%2!=0){
                System.out.println(arr[i]);
            }
        
            
        }
        
        
    }}
    

