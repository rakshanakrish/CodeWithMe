package basics;
import java.util.Scanner;

public class StudData {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of students: ");
        int a = scan.nextInt();
        System.out.print("Enter number of subjects: ");
        int b = scan.nextInt();
        
        for(int i = 1;i<=a;i++){
            String name = scan.nextLine();
            System.out.println("Enter name of the students: ");
            scan.nextLine();
            int total = 0;
            int marks[] = new int[b];
                marks[i] = scan.nextInt();
                total +=marks[i];
            for(int j=0;j<=b;j++){
                System.out.println("Enter mark"+(j+1)+ ":");
            }
            double avg = total /b;
                System.out.print("Total marks: "+total);
                System.out.print("Average: "+avg);
    }}
}
