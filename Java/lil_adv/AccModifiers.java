package lil_adv;

class AccModifiers {
    String name;
    int rollno;

    private void display() {
        System.out.println(name);
        System.out.println(rollno);}
    
    public void setVal(String str, int num){
        name = "str";
        rollno = 1;

    }
    public void disp(){
        System.out.println(name);
    }

}
class another{
    public static void main(String[] args) {
        AccModifiers obj = new AccModifiers();
        obj.setVal("Rakshana",67);
        obj.display();

    }


}
