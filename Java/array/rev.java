package array;

public class rev {
    public static void main(String[] args) {
        int[]arr = {1,2,3,4,5};
        int temp = 0;
        for(int i =0;i<arr.length-1;i++){
            for(int j =0;j<arr.length-1-i;j++){
                if(arr[j]!=arr[j+1]){
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
        }}
        System.out.println(arr[i]);
    }
    
}}
