import java.util.Scanner;
public class prac {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int score = scan.nextInt();
        if (score <50){
            System.out.println("Need to improve");
        }
        else if (score ==50 || score >50 && score <70){
            System.out.println("well done");
        }
        else if (score>70){
            System.out.println("excellent");
        }

    }

}
