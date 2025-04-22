package lil_adv;
public class classObj {
    String name;
    int rollno;
   
    public void display() {
        System.out.println(name);
        System.out.println(rollno);}

public static void main(String[] args) {
    classObj att = new classObj(); //new for memory allocation
    att.name = "Rakshana";
    att.rollno = 67;
    att.display();
        }

    
}
