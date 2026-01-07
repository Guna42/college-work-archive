class LoginCheck {
    public static void main(String[] args) {
        String username = "admin";
        String password = "1234";

        String enteredUser = "admin";
        String enteredPass = "1234";

        System.out.println("Enter username: " + enteredUser);
        System.out.println("Enter password: " + enteredPass);

        if (enteredUser.equals(username) && enteredPass.equals(password)) {
            System.out.println("Login successful!");
        } else {
            System.out.println("Invalid credentials.");
        }
    }
}
