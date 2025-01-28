//print the two digit numbers
package array;
import java.util.*;
public class two {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int []arr = new int[100];
        for(int i =0;i<arr.length;i++){
            arr[i]= sc.nextInt();
            if(arr[i]>9 && arr[i]<100){
                System.out.println(arr[i]);
            }
        }
        
    }
    
}
