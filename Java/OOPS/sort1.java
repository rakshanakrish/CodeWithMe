package OOPS;  ////not yet completed
import java.util.Scanner;

public class sort1 {

    static void selectionSort(int[]arr,int n){
        for(int i =0;i<n-1;i++){
            for(int j =i+1;j<n;j++){
                if(arr[i]>arr[j]){
                int temp = arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }}
        }

    }

    static void calculation(int a,int b){
        int add = a+b;
        int mul = a*b;
        int div = a/b;
        System.out.print("Addition: "+add);
        System.out.print("Product: "+mul);
        System.out.print("Division: "+div);
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();
        System.out.print("Enter the elements of array: ");
        int[] arr = new int[n];
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
        selectionSort(arr, n);
        System.out.print("the sorted array is ");
        for(int i=0;i<n;i++)
        System.out.print(arr[i]+" ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        calculation(a, b);
    }
    
}