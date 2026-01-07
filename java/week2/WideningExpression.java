public class WideningExpression {
    public static void main(String[] args) {
        int a = 10;
        float b = 3.2f;
        float result = a * b + a / b;
        System.out.println("a (int): " + a);
        System.out.println("b (float): " + b);
        System.out.println("Result (float): " + result);
    }
}
