public class Fib {

    // Static variable to mimic a global variable
    static int count = 2;

    public static void main(String[] args) {
        // Print the first two Fibonacci numbers
        System.out.println(0);
        System.out.println(1);

        // Start the recursion
        fibonacci(1, 0);
    }

    // Recursive method to print Fibonacci numbers
    public static void fibonacci(int prev1, int prev2) {
        if (count <= 19) { // Print only 20 Fibonacci numbers
            int newFibo = prev1 + prev2; // Calculate the next Fibonacci number
            System.out.println(newFibo);

            // Update the counter
            count++;

            // Recursive call with updated values
            fibonacci(newFibo, prev1);
        } else {
            // Base case: stop recursion
            return;
        }
    }
}

