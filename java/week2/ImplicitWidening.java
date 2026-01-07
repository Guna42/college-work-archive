public class ImplicitWidening {
    public static void main(String[] args) {
        byte byteValue = 12;
        short shortValue = byteValue;
        int intValue = shortValue;
        long longValue = intValue;
        System.out.println("byte value: " + byteValue);
        System.out.println("short value: " + shortValue);
        System.out.println("int value: " + intValue);
        System.out.println("long value: " + longValue);
    }
}
