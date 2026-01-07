public class ElectricityBill {
    public static void main(String[] args) {
        int units = 120;
        int rate = 5;
        int bill = units * rate;
        bill += 50;
        System.out.println("Total Bill: ₹" + bill);
    }
}


