class MaxOfThree {
    public static void main(String[] args) {
        int a = 15, b = 25, c = 20;

        System.out.println("Enter a: " + a);
        System.out.println("Enter b: " + b);
        System.out.println("Enter c: " + c);

        int max = a;
        if (b > max) max = b;
        if (c > max) max = c;

        System.out.println("Maximum: " + max);
    }
}
