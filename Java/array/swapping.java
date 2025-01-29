//swaping of array
package array;
import java.util.*;
public class swapping {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int temp=0;
        int []arr={6,4,8,2,5};
        int index1=sc.nextInt();
        int index2=sc.nextInt();
        temp=arr[index1];
        arr[index1]=arr[index2];
        arr[index2]=temp;
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]);
        }

        
    }
    
}

