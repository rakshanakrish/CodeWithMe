//take two array
package array;

public class summa {
    public static void main(String[] args) {
        int[]arr1={1,2,4,5,8,9};
        int[]arr2={3,5,7,9,6,8};
        System.out.print("Array1: ");
        int temp =0;
        for(int i=0;i<arr1.length;i++){
            temp =arr1[i];
            arr1[i] = arr2[i];
            arr2[i] = temp;
    }
    
     for(int i:arr1){
         System.out.print(i+" ");
    }
     System.out.println();
     System.out.print("Array2: ");
     for(int i:arr2){
         System.out.print(i+" ");
     }
    
}
}
