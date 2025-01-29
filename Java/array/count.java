//count numbers ending with 5
package array;

public class count {
    public static void main(String[] args) {
        int[] arr = {15, 20, 35, 42, 5};
        int count= 0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]%10==5){
                count++;
                //System.out.println(arr[i]);
            }}
            System.out.println(count);
    }
}
