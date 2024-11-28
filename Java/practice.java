import java.lang.System;
import java.util.Scanner;

public class practice {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String RCB = scan.nextLine();
        if(RCB.equalsIgnoreCase("Wins"))
        {
            System.out.println("Ee saala cup namathe");
        }
        else{
            System.out.println("Cup uh poche");

        }
        scan.close();

    }
}
