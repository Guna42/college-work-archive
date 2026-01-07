import java.util.*;
class Fibo{
    public static void main(String[] args){
        int n = new Scanner(System.in).nextInt();
        int a = 0, b = 1;
        for(int i = 0; i < n; i++){
            System.out.print(a + " ");
            int c = a + b;
            a = b;
            b = c;
        }
    }
}
