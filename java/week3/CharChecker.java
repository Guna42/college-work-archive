class CharChecker {
    public static void main(String[] args) {
        char ch = 'a';

        System.out.println("Enter character: " + ch);

        if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z')) {
            System.out.println("Alphabet");
        } else if (ch >= '0' && ch <= '9') {
            System.out.println("Digit");
        } else {
            System.out.println("Special Symbol");
        }
    }
}
