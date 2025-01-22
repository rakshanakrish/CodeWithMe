import java.util.*;
class ElseIf{
    public static void main(String args[])
    {
        int score= 62;


        if(score>35 && score<60){
            System.out.println("video game");
        }
        else if(score>60 && score<90){ //unnecessory checking can be avoided using else if
            System.out.println("iphone");
        }
        else if(score>90){
            System.out.println("mac book");
        }
    }

} 