class GradeAssignment {
    public static void main(String[] args) {
        int marks = 85;

        System.out.println("Enter marks: " + marks);

        if (marks >= 90 && marks <= 100) {
            System.out.println("Grade: A");
        } else if (marks >= 80) {
            System.out.println("Grade: B");
        } else if (marks >= 70) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: F");
        }
    }
}
