package basics;
import java.util.Scanner;

public class ifelse {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        System.out.println(a!=b);


        
        if(a>b)
        {
            System.out.println("a is greater than b");
        }
        else{
            System.out.println("b is greater than a");
        }
    }
}
