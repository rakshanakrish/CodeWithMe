public class twostrg {
    public static void main(String args[])
    {
        String f1 = new String("apple"); //new string uses different objects 
        String f2 = new String("apple");
        //in java there are 2 mry (Stack and heap(String pool))
        //stack - int..., heap - objects

        String a = "orange"; //string uses same reference id
        String b = "orange";

        System.out.println("1."+(f1==f2)); //if we put ("1."+f1==f2) it acts like (("1."+f1)==f2)
        System.out.println("2."+(a==b));
        System.out.print("3."+f1.equals(f2));

    }
    
}
