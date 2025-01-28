package array;
import java.util.Scanner;

public class sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[100];
        int sum = 0;
        System.out.println("Enter numbers (enter 0 to stop):");

        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt(); // Read input
            if (arr[i] == 0) {     // Stop input if 0 is entered
                break;
            }
            sum += arr[i];         // Add to sum if not 0
        }
        
        System.out.println("Sum of entered numbers: " + sum);
    }
}
