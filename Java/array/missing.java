//Finding missing values in an array
package array;
import java.util.*;
public class missing {
    public static void main(String[] args) {
        int[]arr = {1,2,3,5,6,8};
        Arrays.sort(arr);
        for(int i=0;i<arr.length-1;i++){
            int sum=0;
            for(int j=i+1;j<arr.length;j++){
            sum=arr[i]+arr[j];
            break;
            }
            if(sum%2==0){
            System.out.println(sum/2);
        }}

    }
    
}
