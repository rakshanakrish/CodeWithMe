public class nestedif {
    public static void main(String args[])
    {
        boolean kfc = true;
        boolean chicken = true;
        boolean pepsi = true;

        if (kfc){
            System.out.println("Enter into kfc");
            if (chicken){
                System.out.println("Eating chicken");
                if (pepsi){
                    System.out.println("Drinking pepsi");
                }
            }
        }
        

    }
    
}
