class UpiPaymentTracker {
    public static void main(String[] args) {
        String upiID = "guna42@upi";
        float initialBalance = 5000.0f;
        float paymentAmount = 1200.0f;

        float updatedBalance = initialBalance - paymentAmount;

        System.out.println("----- UPI Payment Tracker -----");
        System.out.println("UPI ID: " + upiID);
        System.out.println("Initial Balance: " + initialBalance);
        System.out.println("Payment Amount: " + paymentAmount);
        System.out.println("Updated Balance: " + updatedBalance);
    }
}
