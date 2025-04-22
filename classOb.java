package lil_adv;
class students
{
    int Age;
    int Reg_no;
    String Name;
}
class StudentDetails
{
    public static void main(String[] args) {
        students s1 = new students();
        s1.Age = 20;
        s1.Reg_no = 7128;
        s1.Name = "Rakshana";
     System.out.println(s1.Name);
     students s2 = new students();
     s2.Age = 21;
     s2.Reg_no = 7129;
     System.out.println(s2.Age);
    }
}