import java.util.Scanner;
public class RailwayReservation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] seats = new int[10];
        int choice;
        do {
            System.out.println("\n--- Railway Reservation System ---");
            System.out.println("1. Display Seat Availability");
            System.out.println("2. Book a Seat");
            System.out.println("3. Cancel a Seat");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            switch (choice) {
                case 1:
                    for (int i = 0; i < seats.length; i++) {
                        System.out.println("Seat " + (i + 1) + ": " + seats[i]);
                    }
                    break;
                case 2:
                    System.out.print("Enter seat number to book (1-10): ");
                    int bookSeat = sc.nextInt();
                    if (bookSeat < 1 || bookSeat > 10) {
                        System.out.println("Invalid seat number.");
                    } else if (seats[bookSeat - 1] == 1) {
                        System.out.println("Seat already booked!");
                    } else {
                        seats[bookSeat - 1] = 1;
                        System.out.println("Seat " + bookSeat + " booked successfully.");
                    }
                    break;
                case 3:
                    System.out.print("Enter seat number to cancel (1-10): ");
                    int cancelSeat = sc.nextInt();
                    if (cancelSeat < 1 || cancelSeat > 10) {
                        System.out.println("Invalid seat number.");
                    } else if (seats[cancelSeat - 1] == 0) {
                        System.out.println("Seat is already empty.");
                    } else {
                        seats[cancelSeat - 1] = 0;
                        System.out.println("Seat " + cancelSeat + " canceled successfully.");
                    }
                    break;
                case 4:
                    System.out.println("Exiting System...");
                    break;
                default:
                    System.out.println("Invalid choice, try again.");
            }
        } while (choice != 4);
    }
}
