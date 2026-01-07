import java.util.Scanner;

public class StudentResults {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] marks = new int[5][3];
        int[] total = new int[5];
        double[] avg = new double[5];

        System.out.println("Enter marks of 5 students (3 subjects each):");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 3; j++) {
                marks[i][j] = sc.nextInt();
            }
        }

        System.out.println("\nMarks of Students:");
        for (int i = 0; i < 5; i++) {
            System.out.print("Student " + (i + 1) + ": ");
            for (int j = 0; j < 3; j++) {
                System.out.print(marks[i][j] + " ");
                total[i] += marks[i][j];
            }
            avg[i] = total[i] / 3.0;
            System.out.println("| Total: " + total[i] + " | Avg: " + avg[i]);
        }

        int topper = 0;
        for (int i = 1; i < 5; i++) {
            if (total[i] > total[topper]) {
                topper = i;
            }
        }
        System.out.println("\nTopper is Student " + (topper + 1) + " with " + total[topper] + " marks.");

        int pass = 0, fail = 0;
        for (int i = 0; i < 5; i++) {
            if (avg[i] >= 40) pass++;
            else fail++;
        }
        System.out.println("Passed Students: " + pass);
        System.out.println("Failed Students: " + fail);
    }
}
