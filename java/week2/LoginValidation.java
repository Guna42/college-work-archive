public class LoginValidation {
    public static void main(String[] args) {
        String username = "admin";
        String password = "1234";
        if (username.equals("admin") && password.equals("1234")) {
            System.out.println("Login Successful");
        } else {
            System.out.println("Access Denied");
        }
    }
}
