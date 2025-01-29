//printing array in descending order ///in error
package array;
import java.util.*;
public class desc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[]arr= new int[n];
        for(int i=0;i<arr.length;i++){
            arr[i]=sc.nextInt();
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]>arr[j]){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }}
        }
        for(int i :arr){
            System.out.print(i);
        }

    }
    
}
