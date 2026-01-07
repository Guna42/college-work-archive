import java.util.Scanner;

public class ShoppingCart {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] cart = {1200, 499, 750, 2000, 800, 300}; 

        System.out.println("Items in the cart:");
        for (int price : cart) {
            System.out.print(price + " ");
        }
        System.out.println();

        int min = cart[0], max = cart[0], sum = 0;
        for (int price : cart) {
            if (price < min) min = price;
            if (price > max) max = price;
            sum += price;
        }

        double avg = (double) sum / cart.length;

        System.out.println("Cheapest item: " + min);
        System.out.println("Most expensive item: " + max);
        System.out.println("Total cost: " + sum);
        System.out.println("Average cost: " + avg);

        if (sum >= 5000) {
            double discount = sum * 0.10;
            System.out.println("You get a discount of: " + discount);
            System.out.println("Final Price after discount: " + (sum - discount));
        } else {
            System.out.println("No discount available.");
        }
    }
}
