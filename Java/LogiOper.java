import java.util.Scanner;

public class LogiOper {
    public static void main(String args[])
    {
        System.out.println("Enter an integer:" );
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();


        if(a%3 ==0 || a%5 ==0) //(And &&) //(Or ||)
        {
            System.out.println("divisible by 3 and 5");
        }
        else
        {
            System.out.println("not divisible by 3 and 5");
        }

           
        
    }
}
