package lil_adv;
class sample{
    int rollno;
    int marks;
    sample(int num, int mark){ //default constructor is just sample(){}
        rollno = num;
        marks = mark;
    }

}

class constructors {
    public static void main(String[] args) {
        sample obj = new sample(71,50); //parameterized constructors
        System.out.println(obj.marks);
        System.out.println(obj.rollno);
    }
    
}
