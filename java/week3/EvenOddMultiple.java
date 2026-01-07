class EvenOddMultiple {
    public static void main(String[] args) {
        int num = 10;

        System.out.println("Enter number: " + num);

        if (num % 2 == 0) {
            if (num % 5 == 0) {
                System.out.println("Even and a multiple of 5");
            } else {
                System.out.println("Even but not a multiple of 5");
            }
        } else {
            if (num % 5 == 0) {
                System.out.println("Odd and a multiple of 5");
            } else {
                System.out.println("Odd but not a multiple of 5");
            }
        }
    }
}
