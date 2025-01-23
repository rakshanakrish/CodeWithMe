package lil_adv;

class AccModifiers {
    String name;
    int rollno;

    private void display() {
        System.out.println(name);
        System.out.println(rollno);}
    
    public void setVal(String str, int num){
        name = str;
        rollno = num;
    }
    public void getVal(){
        display(); // Call the private display() method within the class
    }
}
class another{
    public static void main(String[] args) {
        AccModifiers obj = new AccModifiers();
        obj.setVal("Rakshana",67);
        obj.getVal();

    }
}
