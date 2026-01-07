public class StringMethodsDemo {
    public static void main(String[] args) {
        String str1 = "Hello World";
        String str2 = "hello world";
        String emptyStr = "";
        String blankStr = "   ";

        System.out.println("Length of str1: " + str1.length());
        System.out.println("Concatenation: " + str1.concat(" Java"));
        System.out.println("Uppercase: " + str1.toUpperCase());
        System.out.println("Lowercase: " + str1.toLowerCase());

        char ch1 = 'A';
        char ch2 = 'a';
        System.out.println("Is 'A' uppercase? " + Character.isUpperCase(ch1));
        System.out.println("Is 'a' lowercase? " + Character.isLowerCase(ch2));

        System.out.println("Character at index 1: " + str1.charAt(1));
        System.out.println("Is emptyStr empty? " + emptyStr.isEmpty());
        System.out.println("Is blankStr blank? " + blankStr.isBlank());
        System.out.println("Substring from index 6: " + str1.substring(6));
        System.out.println("Substring (0,5): " + str1.substring(0, 5));
        System.out.println("str1 equals str2? " + str1.equals(str2));
        System.out.println("str1 equalsIgnoreCase str2? " + str1.equalsIgnoreCase(str2));
        System.out.println("Index of 'o': " + str1.indexOf('o'));
        System.out.println("Last index of 'o': " + str1.lastIndexOf('o'));
        System.out.println("Does str1 contain 'World'? " + str1.contains("World"));
        System.out.println("Does str1 start with 'Hello'? " + str1.startsWith("Hello"));
    }
}