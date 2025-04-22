/*Write a java program for choosing best plan
 * plan A
 * Day time: 100 min free and 25 paisa per min
 * Evening: 15 paisa per min
 * Night:20 paisa per min
 * plan B
 * Day time: 250 min free and 45 paisa per min
 * Evening: 35 paisa per min
 * Night:25 paisa per min
 */

package functions;

import java.util.Scanner;

public class sum1 {
    static void printDetails(int day,int eve, int ngt){
        double amtA,amtB;
        amtA = (eve*0.15) + (ngt*0.2);
        amtB = (eve*0.15) + (ngt*0.2);
        if(day>100){
            amtA = (day-100) *0.25;
        }
        if(day>250){
            amtB = (day-100) *0.45;
        }
        System.out.println("planA cost : "+amtA);
        System.out.println("planB cost : "+amtB);
        if(amtA>amtB){
            System.out.println("Plan B is best");
        }else{
            System.out.println("Plan A is best");
        }
        
        
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Day timing: ");
        int d = sc.nextInt();
        System.out.print("Enter the Evenng timing: ");
        int e = sc.nextInt();
        System.out.print("Enter the Night timing: ");
        int n = sc.nextInt();
        
        printDetails(d, e, n);

        
    }
}
