package basics;
import java.lang.System;
import java.util.Scanner;

class hello{
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String name = scan.nextLine();
        int age = scan.nextInt();
        System.out.println("My name is "+name);
        System.out.println("My age is "+age);
        
    }
}