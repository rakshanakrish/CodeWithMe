package array;

public class asc {
    public static void main(String[] args) {
        int[]arr = {4,7,9,2,5,1};
        int temp = 0;
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]>arr[j]){ //for descending change the symbol
                temp=arr[j];
                arr[j]=arr[i];
                arr[i]=temp;
            }}
        }
        for(int i:arr){
            System.out.println(i);
        }
        
    }
}
