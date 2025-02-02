package array; //error
import java.util.*;
public class duplicate {
    public static void main(String[] args) {
        int[]arr = {1,2,3,4,4,5,6,6};
        int temp = 1;
        for(int j =0;j<arr.length;j++){
            if(arr[j]!=arr[j-1]){
                arr[temp]=arr[j];
                temp++;
            }
    }
    System.out.println(Arrays.toString(arr));
    for(int j =0;j<temp;j++){
        System.out.println(arr[j]);
    }
    
}}
