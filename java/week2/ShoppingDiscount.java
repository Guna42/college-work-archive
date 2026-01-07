public class ShoppingDiscount {
    public static void main(String[] args) {
        double purchaseAmount = 6000;
        double discount = (purchaseAmount > 5000) ? 0.20 : 0.10;
        double finalAmount = purchaseAmount - (purchaseAmount * discount);
        System.out.println("Final Amount: ₹" + finalAmount);
    }
}
