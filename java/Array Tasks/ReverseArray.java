import java.util.Scanner;

public class ReverseArray {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int n = arr.length;
        System.out.println("Original Array:");
        for (int i : arr) System.out.print(i + " ");
        System.out.println("\nReversed Array:");
        for (int i = n - 1; i >= 0; i--) System.out.print(arr[i] + " ");
    }
}
