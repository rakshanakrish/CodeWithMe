class forloop{
    public static void main(String[] args) {
        int a = 0;
        int b = 1;
        System.out.println(a);
        System.out.println(b);

        for(int i=0; i<18; i++){
            int c = a + b;
            System.out.println(c);
            a = b; //Using int a = b; int b = c; inside the loop is unnecessary
            b = c;

        } 
    }

}