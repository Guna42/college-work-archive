class DiscountCheck {
    public static void main(String[] args) {
        int age = 65;
        double amount = 1200;

        System.out.println("Enter age: " + age);
        System.out.println("Enter amount: " + amount);

        if (age > 60 && amount > 1000) {
            double discount = amount * 0.10;
            double finalAmount = amount - discount;
            System.out.println("Discount Applied: ₹" + discount);
            System.out.println("Final Amount: ₹" + finalAmount);
        } else {
            System.out.println("No discount. Final Amount: ₹" + amount);
        }
    }
}
