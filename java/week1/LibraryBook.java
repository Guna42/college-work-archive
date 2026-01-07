class LibraryBook {
    public static void main(String[] args) {
        String bookTitle = "Java Programming";
        String authorName = "James Gosling";
        int bookID = 12345;
        int daysOverdue = 5;
        double finePerDay = 2.50;

        double totalFine = daysOverdue * finePerDay;

        System.out.println("----- Library Book Info -----");
        System.out.println("Book Title: " + bookTitle);
        System.out.println("Author: " + authorName);
        System.out.println("Book ID: " + bookID);
        System.out.println("Days Overdue: " + daysOverdue);
        System.out.println("Fine Per Day: " + finePerDay);
        System.out.println("Total Fine: " + totalFine);
    }
}
