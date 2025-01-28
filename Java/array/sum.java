package array;
import java.util.Scanner;

public class sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int n = sc.nextInt(); // Array size

        int[] numbers = new int[n];
        System.out.println("Enter the elements of the array:");

        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt(); // Taking user input
        }

        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += numbers[i];
        }

        System.out.println("The sum of the array elements is: " + sum);
    }
}

