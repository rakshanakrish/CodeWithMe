// print even numbers from an array containing numbers from 1 to 100
package array;
import java.util.Scanner;
public class eve {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter the length of array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i+1;
            if(arr[i]%2==0){
                System.out.println(arr[i]);
            }
        }
        
    }
    
}
