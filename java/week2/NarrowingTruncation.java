public class NarrowingTruncation {
    public static void main(String[] args) {
        double originalDouble = 89.67;
        int truncatedValue = (int) originalDouble;
        System.out.println("Original double: " + originalDouble);
        System.out.println("After casting to int: " + truncatedValue);
    }
}
