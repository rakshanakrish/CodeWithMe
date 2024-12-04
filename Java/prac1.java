import java.util.Scanner;

public class prac1 {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int english = scan.nextInt();
        int tamil = scan.nextInt();
        int maths = scan.nextInt();
        int science = scan.nextInt();
        int social = scan.nextInt();

        int totalmarks = (english+tamil+maths+science+social);
        int avg = (english+tamil+maths+science+social)/5;
        System.out.println("Average:"+avg);


        if(avg<50){
            System.out.println("Additional class is required");
        }
        else{
            System.out.println("Good to go");
        }

    }
    
}
