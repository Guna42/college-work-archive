class ATMMenu {
    public static void main(String[] args) {
        int balance = 1000;

        System.out.println("Choose: 1");
        System.out.println("Balance: " + balance);

        System.out.println("Choose: 2");
        int deposit = 500;
        System.out.println("Enter deposit amount: " + deposit);
        balance += deposit;

        System.out.println("Choose: 1");
        System.out.println("Balance: " + balance);

        System.out.println("Choose: 3");
        int withdraw = 300;
        System.out.println("Enter withdrawal amount: " + withdraw);
        balance -= withdraw;

        System.out.println("Choose: 1");
        System.out.println("Balance: " + balance);

        System.out.println("Choose: 4");
        System.out.println("Thank you. Exiting.");
    }
}
