import java.util.Scanner;

public class StudentGrades {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of students: ");
        int n = sc.nextInt();
        int[] grades = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            System.out.print("Enter grade of student " + (i + 1) + ": ");
            grades[i] = sc.nextInt();
            sum += grades[i];
        }
        double avg = (double) sum / n;
        System.out.println("Average grade: " + avg);
    }
}
