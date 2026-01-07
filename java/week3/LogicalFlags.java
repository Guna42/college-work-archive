class LogicalFlags {
    public static void main(String[] args) {
        boolean isStudent = true;
        boolean hasIDCard = true;

        System.out.println("isStudent: " + isStudent);
        System.out.println("hasIDCard: " + hasIDCard);

        if (isStudent && hasIDCard) {
            System.out.println("Access Granted");
        } else {
            System.out.println("Access Denied");
        }
    }
}
